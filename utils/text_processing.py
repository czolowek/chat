import re
from typing import List, Set

def normalize_text(text: str) -> str:
    # Приводим к нижнему регистру
    text = text.lower()
    
    # Удаляем лишние пробелы
    text = ' '.join(text.split())
    
    # Удаляем или заменяем некоторые специальные символы
    text = re.sub(r'[^\w\s\-,.?!():]', ' ', text)
    
    # Заменяем многоточие на точку
    text = re.sub(r'\.{2,}', '.', text)
    
    # Заменяем множественные пробелы на один
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def extract_keywords(text: str, keywords: Set[str]) -> List[str]:
    found_keywords = []
    
    for keyword in keywords:
        # Ищем ключевое слово как отдельное слово в тексте
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            found_keywords.append(keyword)
    
    return found_keywords

def split_into_sentences(text: str) -> List[str]:
    # Используем регулярное выражение для разбиения по знакам препинания,
    # но учитываем, что точка может быть частью сокращения или числа
    sentences = re.split(r'(?<!\w\.\w.)(?<![А-Я][а-я]\.)(?<=\.|\?|\!)\s', text)
    return [sent.strip() for sent in sentences if sent.strip()]

def is_question(text: str) -> bool:
    # Проверяем наличие вопросительного знака
    if '?' in text:
        return True
    
    # Проверяем начало текста с вопросительных слов
    question_words = [
        'что', 'кто', 'где', 'когда', 'почему', 'зачем', 'как', 'сколько',
        'какой', 'какая', 'какое', 'какие', 'чей', 'чья', 'чьё', 'чьи'
    ]
    
    first_word = text.split()[0].lower() if text.split() else ''
    return first_word in question_words
