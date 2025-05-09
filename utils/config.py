# -*- coding: utf-8 -*-
import os

# Токен Telegram бота
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8194190025:AAE_CMGzm2zBSCqeOco0vYzXVOPHO1O8_HY")

# Настройки логирования
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DIR = "logs"

# Максимальное время хранения состояния пользователя (в секундах)
# По умолчанию 1 час
USER_STATE_TIMEOUT = int(os.environ.get("USER_STATE_TIMEOUT", 3600))

# Настройки для модулей
MODULE_SETTINGS = {
    "adaptatsiya": {
        "enabled": True,
        "priority": 1
    },
    "matematika": {
        "enabled": True,
        "priority": 2
    },
    "fizika": {
        "enabled": True,
        "priority": 3
    },
    "biologiya": {
        "enabled": True,
        "priority": 4
    },
    "khimiya": {
        "enabled": True,
        "priority": 5
    },
    "geografiya": {
        "enabled": True,
        "priority": 6
    },
    "istoriya": {
        "enabled": True,
        "priority": 7
    }
}