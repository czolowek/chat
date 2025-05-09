from utils.config import MODULE_SETTINGS

# Список доступных модулей
AVAILABLE_MODULES = [module for module, settings in MODULE_SETTINGS.items() if settings.get("enabled", False)]

# Словарь для кэширования состояний пользователей
USER_STATES = {}
