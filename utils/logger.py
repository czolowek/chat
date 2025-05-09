import logging
import os
from logging.handlers import RotatingFileHandler
import sys

from config import LOG_LEVEL, LOG_FORMAT, LOG_DIR

def setup_logger(name: str) -> logging.Logger:

    # Создаем директорию для логов, если ее нет
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    # Создаем логгер
    logger = logging.getLogger(name)
    
    # Устанавливаем уровень логирования
    level = getattr(logging, LOG_LEVEL)
    logger.setLevel(level)
    
    # Проверяем, не добавлены ли уже обработчики
    if not logger.handlers:
        # Создаем обработчик для вывода в файл с ротацией
        # Максимальный размер файла - 5 МБ, хранить до 5 старых файлов
        file_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, f"{name}.log"),
            maxBytes=5*1024*1024,
            backupCount=5
        )
        file_formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        
        # Создаем обработчик для вывода в консоль
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = logging.Formatter(LOG_FORMAT)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
    
    return logger