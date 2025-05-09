import importlib
import re
import logging
from typing import Dict, List, Any
import time

from utils.config import MODULE_SETTINGS
from utils.text_processing import normalize_text
from utils.logger import setup_logger

# Создаем словарь для хранения состояний пользователей
USER_STATES = {}
# Словарь для хранения времени последнего обращения пользователя
USER_LAST_ACTIVITY = {}
# Время, через которое состояние пользователя сбрасывается (в секундах)
from utils.config import USER_STATE_TIMEOUT

# Настройка логгера
logger = setup_logger("router")

# Загрузка модулей
def load_modules():
    """
    Динамически загружает все модули, указанные в настройках
    
    Returns:
        Dict[str, Any]: Словарь с экземплярами модулей
    """
    modules = {}
    for module_name, settings in MODULE_SETTINGS.items():
        if settings.get("enabled", False):
            try:
                # Импортируем модуль динамически
                module_path = f"modules.{module_name}"
                module = importlib.import_module(module_path)
                
                # Ищем класс модуля (предполагается, что имя класса - это название модуля с большой буквы + Module)
                class_name = module_name.capitalize() + "Module"
                if hasattr(module, class_name):
                    module_class = getattr(module, class_name)
                    modules[module_name] = module_class(module_name)
                    logger.info(f"Модуль {module_name} успешно загружен")
                else:
                    logger.error(f"Класс {class_name} не найден в модуле {module_name}")
            except Exception as e:
                logger.error(f"Ошибка при загрузке модуля {module_name}: {str(e)}")
    
    return modules

# Загружаем модули при старте
MODULES = load_modules()

async def route_message(chat_id: int, text: str) -> str:
    # Обновляем время последней активности пользователя
    USER_LAST_ACTIVITY[chat_id] = time.time()
    
    # Очистка устаревших состояний для экономии памяти
    clean_old_states()
    
    # Получаем текущее состояние пользователя
    current_state = USER_STATES.get(chat_id, "start")
    current_module = current_state.split('_')[0] if '_' in current_state else None
    
    # Нормализуем текст для анализа
    normalized_text = normalize_text(text)
    
    # Если текст слишком короткий, просим уточнить
    if len(normalized_text) < 2:
        return "Пожалуйста, напишите более подробный запрос, чтобы я мог помочь."
    
    # Если у пользователя есть активный модуль, сначала проверяем его
    if current_module and current_module in MODULES:
        module = MODULES[current_module]
        # Проверяем, релевантен ли запрос текущему модулю
        if module.matches(normalized_text) or module.get_confidence(normalized_text) > 0.3:
            logger.info(f"Продолжаем использовать текущий модуль: {current_module}")
            response, new_state = module.get_response(text, current_state)
            USER_STATES[chat_id] = new_state
            return response
    
    # Если нет активного модуля или запрос не релевантен текущему, выбираем новый модуль
    best_module = None
    best_confidence = 0.0
    
    for module_name, module in MODULES.items():
        confidence = module.get_confidence(normalized_text)
        if confidence > best_confidence:
            best_confidence = confidence
            best_module = module_name
    
    # Если нашли подходящий модуль с достаточной уверенностью
    if best_module and best_confidence > 0.2:
        logger.info(f"Выбран модуль: {best_module} с уверенностью {best_confidence:.2f}")
        module = MODULES[best_module]
        response, new_state = module.get_response(text, "start")
        USER_STATES[chat_id] = new_state
        return response
    
    # Если не нашли подходящий модуль, даем общий ответ
    logger.info("Подходящий модуль не найден, используем общий ответ")
    return (
        "Извините, я не уверен, что понимаю ваш запрос. Вы можете спросить меня "
        "о математике, физике, биологии, химии, географии, истории или других темах. "
        "Пожалуйста, уточните ваш вопрос."
    )

def clean_old_states():
    current_time = time.time()
    to_delete = []
    
    for chat_id, last_activity in USER_LAST_ACTIVITY.items():
        if current_time - last_activity > USER_STATE_TIMEOUT:
            to_delete.append(chat_id)
    
    for chat_id in to_delete:
        if chat_id in USER_STATES:
            del USER_STATES[chat_id]
        del USER_LAST_ACTIVITY[chat_id]
    
    if to_delete:
        logger.info(f"Очищено {len(to_delete)} устаревших состояний пользователей")
