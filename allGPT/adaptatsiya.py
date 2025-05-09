import random
import re
from typing import Tuple, Set

from allGPT.base import BaseModule
from utils.text_processing import normalize_text

class AdaptatsiyaModule(BaseModule):
    def _init_keywords(self) -> Set[str]:
        return {
            'адаптация', 'адаптироваться', 'приспособиться', 'меняться',
            'изменения', 'перемены', 'новые условия', 'адаптивность',
            'приспосабливаться', 'адаптирование', 'гибкость', 'преобразование',
            'стресс', 'выживание', 'развитие', 'поддержка'
        }
    
    def get_response(self, text: str, current_state: str) -> Tuple[str, str]:
        normalized_text = normalize_text(text)
        new_state = current_state
        
        if len(normalized_text) < 3:
            response = 'Пожалуйста, напишите подробнее.'
            return response, new_state
            
        if 'что такое адаптация' in normalized_text or 'объясни адаптацию' in normalized_text:
            response = ('Адаптация — это процесс приспосабливания к новым условиям. '
                        'Почему, по-твоему, умение адаптироваться так важно?')
            new_state = 'asked_definition'
        elif ('не знаю' in normalized_text and 'адаптация' in normalized_text) or 'не понимаю адаптацию' in normalized_text:
            response = ('Адаптация помогает меняться и расти. '
                        'Расскажи, какие изменения произошли в твоей жизни?')
            new_state = 'explained_adaptation'
        elif any(phrase in normalized_text for phrase in ['ты адаптировался', 'тебе удалось адаптироваться', 'как ты адаптируешься']):
            response = ('Я, как программа, постоянно учусь и изменяюсь. '
                        'Расскажи, что для тебя самое сложное в адаптации?')
            new_state = 'asked_personal'
        elif 'как адаптироваться' in normalized_text or ('адаптироваться' in normalized_text and 'как' in normalized_text):
            response = ('Обычно помогает уверенность в себе и поддержка близких. '
                        'Какие стратегии ты используешь для адаптации?')
            new_state = 'strategy_question'
        elif current_state in ['asked_definition', 'explained_adaptation', 'asked_personal', 'strategy_question']:
            if any(word in normalized_text for word in ['понятно', 'ясно', 'да', 'согласен']):
                response = 'Отлично! Можешь поделиться примером из своего опыта?'
                new_state = 'example_request'
            elif any(word in normalized_text for word in ['нет', 'не понимаю', 'сложно']):
                response = 'Понимаю, что адаптация бывает непростой. Что именно вызывает трудности?'
                new_state = 'challenge_discussion'
            else:
                response = 'Расскажи подробнее о своих мыслях на этот счёт.'
                new_state = 'general_followup'
        elif 'адапта' in normalized_text:
            options = [
                'Адаптация может быть сменой работы. Как ты к этому относишься?',
                'Жизнь постоянно меняется. Какие перемены были для тебя значимыми?',
                'Приспособление к новым условиям — важный навык. Есть у тебя примеры?'
            ]
            response = random.choice(options)
            new_state = 'general_adaptation'
        elif 'проблема' in normalized_text:
            response = 'Проблемы часто заставляют нас меняться. С какими трудностями ты сталкивался?'
            new_state = 'problem_discussion'
        elif 'успех' in normalized_text:
            response = 'Успех приходит, когда мы умеем адаптироваться. Что для тебя означает успех?'
            new_state = 'success_discussion'
        elif 'изменение' in normalized_text:
            response = 'Изменения — неотъемлемая часть жизни. Какие перемены повлияли на тебя?'
            new_state = 'change_discussion'
        elif 'жизнь' in normalized_text and 'адапт' in normalized_text:
            response = 'Жизнь полна сюрпризов. Как ты справляешься с неожиданными переменами?'
            new_state = 'life_discussion'
        elif 'новый опыт' in normalized_text:
            response = 'Новый опыт всегда приносит уроки. Что нового ты пробовал недавно?'
            new_state = 'new_experience'
        elif 'приспосабливаться' in normalized_text:
            response = 'Умение приспосабливаться закаляет нас. Какие методы помогают тебе в этом?'
            new_state = 'skill_development'
        elif 'перемены' in normalized_text:
            response = 'Перемены могут быть радостными или пугающими. Как ты их воспринимаешь?'
            new_state = 'change_attitude'
        elif 'адаптивность' in normalized_text:
            response = 'Адаптивность — залог успеха. Что, по-твоему, помогает людям быть адаптивными?'
            new_state = 'adaptability_discussion'
        elif 'новые условия' in normalized_text:
            response = 'Новые условия требуют свежего подхода. С какими новыми условиями ты сталкивался?'
            new_state = 'new_conditions'
        elif 'подстраиваться' in normalized_text:
            response = 'Подстраиваться под обстоятельства — это искусство. Расскажи, когда тебе пришлось подстраиваться.'
            new_state = 'adjustment_story'
        else:
            response = 'Давай поговорим об адаптации. Что для тебя значит меняться и приспосабливаться к жизни?'
            new_state = 'initial_response'
        
        return response, new_state
