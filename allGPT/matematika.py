import random
import re
from typing import Tuple, Set, Dict, List
import math

from allGPT.base import BaseModule
from utils.text_processing import normalize_text

class MatematikaModule(BaseModule):
    """Модуль для обработки запросов по теме 'Математика'"""
    
    def _init_keywords(self) -> Set[str]:
        """Инициализация ключевых слов для модуля математики"""
        return {
            'математика', 'вычислить', 'посчитать', 'решить', 'число',
            'уравнение', 'формула', 'алгебра', 'геометрия', 'тригонометрия',
            'площадь', 'объем', 'периметр', 'теорема', 'функция', 'график',
            'значение', 'интеграл', 'производная', 'предел', 'матрица',
            'система', 'корень', 'степень', 'логарифм', 'вероятность',
            'синус', 'косинус', 'тангенс', 'котангенс', 'арксинус', 'арккосинус',
            'арктангенс', 'арккотангенс', 'радиан', 'градус', 'вектор', 'скаляр'
        }
    
    def get_response(self, text: str, current_state: str) -> Tuple[str, str]:
        """
        Генерирует ответ на запрос пользователя по теме математики
        
        Args:
            text (str): Текст запроса пользователя
            current_state (str): Текущее состояние диалога
            
        Returns:
            Tuple[str, str]: Кортеж (ответ_бота, новое_состояние)
        """
        normalized_text = normalize_text(text)
        new_state = current_state
        
        # Проверка на короткие запросы
        if len(normalized_text) < 3:
            response = 'Пожалуйста, задайте более подробный вопрос по математике.'
            return response, new_state
        
        # Проверка на простые арифметические операции
        arithmetic_match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', normalized_text)
        if arithmetic_match:
            try:
                num1 = int(arithmetic_match.group(1))
                operator = arithmetic_match.group(2)
                num2 = int(arithmetic_match.group(3))
                
                result = None
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/' and num2 != 0:
                    result = num1 / num2
                
                if result is not None:
                    return f"Результат вычисления {num1} {operator} {num2} = {result}", "math_calculation"
            except Exception as e:
                pass  # В случае ошибки, продолжаем обработку запроса
        
        # Обработка запросов по тригонометрии
        if any(word in normalized_text for word in ['синус', 'косинус', 'тангенс', 'котангенс']):
            if 'синус' in normalized_text:
                trig_match = re.search(r'синус\s+(\d+)', normalized_text)
                if trig_match:
                    try:
                        angle = int(trig_match.group(1))
                        # Преобразуем в радианы
                        rad = math.radians(angle)
                        result = math.sin(rad)
                        return f"Синус {angle} градусов = {result:.4f}", "math_trigonometry"
                    except Exception as e:
                        return "Для вычисления синуса укажите угол в градусах, например: 'синус 30'", "math_trigonometry_error"
            
            return "Для вычисления тригонометрических функций, укажите угол в градусах.", "math_trigonometry_help"
        
        # Обработка запросов по геометрии
        if any(word in normalized_text for word in ['площадь', 'объем', 'периметр']):
            if 'площадь круга' in normalized_text:
                radius_match = re.search(r'радиус(?:ом)?\s+(\d+(?:\.\d+)?)', normalized_text)
                if radius_match:
                    try:
                        radius = float(radius_match.group(1))
                        area = math.pi * radius**2
                        return f"Площадь круга с радиусом {radius} = {area:.4f}", "math_geometry_circle"
                    except Exception as e:
                        pass
            
            if 'площадь квадрата' in normalized_text:
                side_match = re.search(r'сторон(?:ой|ами)?\s+(\d+(?:\.\d+)?)', normalized_text)
                if side_match:
                    try:
                        side = float(side_match.group(1))
                        area = side**2
                        return f"Площадь квадрата со стороной {side} = {area}", "math_geometry_square"
                    except Exception as e:
                        pass
            
            return "Для расчета площади или объема укажите фигуру и её размеры.", "math_geometry_help"
        
        # Общая обработка различных запросов по математике
        if 'что такое математика' in normalized_text or 'объясни математику' in normalized_text:
            response = ('Математика — это наука о структурах, порядке и отношениях, '
                       'которая исторически сложилась на основе операций подсчёта, '
                       'измерения и описания форм реальных объектов. '
                       'Какая область математики вас интересует: алгебра, геометрия, анализ?')
            new_state = 'math_introduction'
        
        elif 'теорема пифагора' in normalized_text:
            response = ('Теорема Пифагора гласит, что в прямоугольном треугольнике квадрат длины гипотенузы '
                       'равен сумме квадратов длин катетов: a² + b² = c², где c — длина гипотенузы, '
                       'a и b — длины катетов. Хотите пример расчета?')
            new_state = 'math_pythagorean'
        
        elif 'как решить квадратное уравнение' in normalized_text or 'квадратное уравнение' in normalized_text:
            response = ('Для решения квадратного уравнения ax² + bx + c = 0 используйте формулу: '
                       'x = (-b ± √(b² - 4ac))/2a. Дискриминант D = b² - 4ac определяет количество корней: '
                       'D > 0 — два корня, D = 0 — один корень, D < 0 — нет действительных корней. '
                       'Хотите решить конкретное уравнение?')
            new_state = 'math_quadratic'
        
        elif current_state == 'math_introduction':
            if 'алгебра' in normalized_text:
                response = ('Алгебра изучает операции над математическими объектами и их свойства. '
                           'Интересует элементарная алгебра (уравнения, многочлены) или высшая (теория групп, колец)?')
                new_state = 'math_algebra'
            elif 'геометрия' in normalized_text:
                response = ('Геометрия изучает пространственные структуры и отношения. '
                           'Вас интересует планиметрия (плоские фигуры) или стереометрия (объемные тела)?')
                new_state = 'math_geometry'
            elif 'анализ' in normalized_text:
                response = ('Математический анализ изучает функции и их обобщения через понятия предела, '
                           'непрерывности, производной, интеграла. Что конкретно вас интересует?')
                new_state = 'math_calculus'
            else:
                response = ('В математике много разделов: алгебра, геометрия, математический анализ, '
                           'теория вероятностей, математическая логика, теория чисел и другие. '
                           'Какой раздел вас интересует больше всего?')
                new_state = 'math_introduction'
        
        elif current_state == 'math_algebra' or 'алгебра' in normalized_text:
            response = ('В алгебре рассматриваются уравнения, системы уравнений, неравенства, '
                       'многочлены, матрицы и их свойства. Могу рассказать подробнее о любой из этих тем.')
            new_state = 'math_algebra_details'
        
        elif current_state == 'math_geometry' or 'геометрия' in normalized_text:
            response = ('Геометрия изучает свойства фигур на плоскости и в пространстве. '
                       'К базовым понятиям относятся точка, прямая, плоскость, расстояние, угол. '
                       'Хотите узнать о конкретных фигурах или формулах?')
            new_state = 'math_geometry_details'
        
        else:
            # Случайные ответы на общие вопросы по математике
            general_responses = [
                'Математика — универсальный язык науки. Какая тема вас интересует?',
                'Интересно, что математика существует во всех культурах. У вас есть конкретный вопрос?',
                'Математика помогает описывать мир формулами и уравнениями. Что бы вы хотели узнать?',
                'В математике красота часто связана с простотой. Какую область вы хотите изучить?',
                'Математика — это не только цифры, но и структуры, логика, причинно-следственные связи. Что конкретно вас интересует?'
            ]
            response = random.choice(general_responses)
            new_state = 'math_general'
        
        return response, new_state
