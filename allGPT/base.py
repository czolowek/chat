# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import re
from typing import Tuple, Dict, List, Set, Optional

class BaseModule(ABC):
    """
    Базовый абстрактный класс для всех модулей предметных областей
    """
    def __init__(self, name: str):
        self.name = name
        self.keywords = self._init_keywords()
    
    @abstractmethod
    def _init_keywords(self) -> Set[str]:
        """
        Инициализация ключевых слов для определения, относится ли запрос к данному модулю
        Должна быть реализована в каждом конкретном модуле
        
        Returns:
            Set[str]: Множество ключевых слов
        """
        pass
    
    def matches(self, text: str) -> bool:
        """
        Проверяет, относится ли текст к данной предметной области
        
        Args:
            text (str): Нормализованный текст запроса
            
        Returns:
            bool: True, если запрос относится к данной предметной области
        """
        # Проверяем наличие ключевых слов
        for keyword in self.keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                return True
        return False
    
    def get_confidence(self, text: str) -> float:
        """
        Вычисляет уровень уверенности, что запрос относится к данной предметной области.
        
        Args:
            text (str): Нормализованный текст запроса
            
        Returns:
            float: Значение от 0.0 до 1.0, показывающее уровень уверенности
        """
        if not text:
            return 0.0
            
        # Подсчет количества ключевых слов в тексте
        count = 0
        for keyword in self.keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                count += 1
        
        # Базовый уровень уверенности зависит от количества найденных ключевых слов
        return min(1.0, count / max(5, len(text.split())))
    
    @abstractmethod
    def get_response(self, text: str, current_state: str) -> Tuple[str, str]:
        """
        Генерирует ответ на запрос пользователя, учитывая текущее состояние диалога
        
        Args:
            text (str): Текст запроса пользователя
            current_state (str): Текущее состояние диалога
            
        Returns:
            Tuple[str, str]: Кортеж (ответ_бота, новое_состояние)
        """
        pass
    
    def normalize_text(self, text: str) -> str:
        """
        Нормализует текст запроса, приводя его к нижнему регистру и удаляя ненужные символы
        
        Args:
            text (str): Исходный текст
            
        Returns:
            str: Нормализованный текст
        """
        # Приводим к нижнему регистру
        text = text.lower()
        # Удаляем лишние пробелы
        text = ' '.join(text.split())
        return text
