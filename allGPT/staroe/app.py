# import asyncio
# import random
# import re
# import os
# import logging
# import nest_asyncio
# from staroe.idea import IDEA_PROJECTS
# from staroe.slowa import EXTENDED_RESPONSES  # словарь с «бесполезными», но интересными фактами
# from telegram import Update, ReplyKeyboardRemove
# from telegram.ext import Application, CommandHandler, MessageHandler, filters
# from staroe.comnerrors import COMMON_ERRORS
# import torch
# import torch.nn as nn
# from PIL import Image, ImageDraw, ImageFont

# # from allGPT.config import BOT_TOKEN

# nest_asyncio.apply()

# # --- НАСТРОЙКА ЛОГИРОВАНИЯ ---
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# # --- УПРАВЛЕНИЕ ДИАЛОГОВОЙ ИСТОРИЕЙ ---
# conversation_history = {}
# MAX_CONTEXT = 20  # теперь история охватывает до 20 сообщений

# def update_conversation(chat_id: int, message: str) -> None:
#     if chat_id not in conversation_history:
#         conversation_history[chat_id] = []
#     conversation_history[chat_id].append(message)
#     if len(conversation_history[chat_id]) > MAX_CONTEXT:
#         conversation_history[chat_id] = conversation_history[chat_id][-MAX_CONTEXT:]

# def get_context(chat_id: int) -> str:
#     return " ".join(conversation_history.get(chat_id, []))

# # --- НЕЙРОСЕТЕВАЯ ЗАГЛУШКА ---
# class ConversationalAI(nn.Module):
#     def __init__(self, input_size: int, hidden_size: int, output_size: int):
#         super(ConversationalAI, self).__init__()
#         self.layer1 = nn.Linear(input_size, hidden_size)
#         self.activation = nn.ReLU()
#         self.layer2 = nn.Linear(hidden_size, output_size)
    
#     def forward(self, x: torch.Tensor) -> torch.Tensor:
#         return self.layer2(self.activation(self.layer1(x)))

# model = ConversationalAI(10, 20, 10)
# tokenizer = lambda text: torch.tensor([random.uniform(-1, 1) for _ in range(10)], dtype=torch.float32)

# # --- ФУНКЦИИ ПРЕДОБРАБОТКИ ТЕКСТА ---
# def normalize_word(word: str) -> str:
#     return re.sub(r'^[^a-zA-Zа-яА-ЯёЁ]+', '', word)

# def correct_text(text: str) -> str:
#     words = text.split()
#     corrected_words = [COMMON_ERRORS.get(normalize_word(word).lower(), word) for word in words]
#     return " ".join(corrected_words)

# def fix_missing_spaces(text: str) -> str:
#     """
#     Если в тексте нет или слишком мало пробелов, пытаемся внести разделители для лучшего анализа.
#     """
#     if " " in text:
#         return text
#     common_phrases = ["привет", "настроение", "помоги", "что", "как", "почему", "зачем", "код", "дела", "ты", "сегодня"]
#     for phrase in common_phrases:
#         text = text.replace(phrase, f" {phrase} ")
#     return ' '.join(text.split())

# # --- ЗАГОТОВКИ ОТВЕТОВ ---
# RESPONSES = {
#     "привет": ["Привет! 😃 Как поживаешь?", "Здарова! Рад тебя видеть!", "Привет-привет! Что нового?"],
#     "как дела": ["У меня всё отлично! А у тебя?", "Нормально, а как сам?", "Всё супер!"],
#     "как настроение": ["Настроение супер!", "Чувствую себя прекрасно!", "Отличное настроение!"],
#     "пока": ["Пока! Береги себя!", "До встречи!", "Пока-пока!"],
#     "не умею": ["Не переживай, все мы учимся!", "Ты справишься, главное не сдаваться!", "Продолжай пытаться!"]
# }

# # --- АНАЛИЗ НАСТРОЕНИЯ ---
# SENTIMENT_WORDS = {
#     "отлично": 1.0, "хорошо": 0.8, "супер": 1.0, "рад": 0.9,
#     "люблю": 1.0, "счастлив": 0.9, "неудовлетворительно": -1.0,
#     "плохо": -1.0, "ужасно": -1.0, "отстой": -0.8,
#     "не знаю": -0.5, "расстроен": -1.0, "грусть": -0.9, "печально": -0.8
# }

# SENTIMENT_RESPONSES = {
#     "positive": ["Отличное настроение! Продолжай в том же духе!", "Я рад, что у тебя всё хорошо!"],
#     "negative": ["Не переживай, всё наладится! Ты справишься!", "Держись, плохие моменты пройдут. Я с тобой!"],
#     "neutral": []
# }

# def analyze_sentiment(text: str) -> float:
#     words = text.lower().split()
#     if not words:
#         return 0.0
#     score = 0.0
#     count = 0
#     for word in words:
#         if word in SENTIMENT_WORDS:
#             score += SENTIMENT_WORDS[word]
#             count += 1
#     return score / count if count else 0.0

# def classify_sentiment(score: float) -> str:
#     if score > 0.3:
#         return "positive"
#     elif score < -0.3:
#         return "negative"
#     else:
#         return "neutral"

# def enrich_with_sentiment(response: str, sentence: str) -> str:
#     score = analyze_sentiment(sentence)
#     sentiment = classify_sentiment(score)
#     extra = ""
#     if SENTIMENT_RESPONSES[sentiment]:
#         extra = " " + random.choice(SENTIMENT_RESPONSES[sentiment])
#     return response + extra

# def enrich_response_with_sentiment(response: str, text: str) -> str:
#     """
#     Дополняет ответ поддержкой или радостным приглашением к диалогу.
#     При любом настроении бот выдает положительную фразу для продолжения общения.
#     """
#     score = analyze_sentiment(text)
#     sentiment = classify_sentiment(score)
#     if sentiment == "negative":
#         response += " Я понимаю, что может быть трудно. Давай попробуем разобраться вместе."
#     else:
#         response += " Всегда рад общению и новым вопросам! Если у тебя ещё что-то есть, рассказывай!"
#     return response

# # --- ДИНАМИЧЕСКАЯ ГЕНЕРАЦИЯ ОТВЕТОВ С УЧЕТОМ КОНТЕКСТА ---
# def generate_dynamic_response(user_message: str, conv_context: str) -> str:
#     """
#     Формирует базовый ответ из трёх частей: приветствие, основное сообщение и заключительная фраза.
#     Если разговор уже идет (conv_context не пустой), приветствие не используется.
#     """
#     # Если новый диалог — включаем приветствие, иначе нет
#     greeting = random.choice(["Привет!", "Здравствуйте!", "Добрый день!"]) if not conv_context.strip() else ""
    
#     lower_msg = user_message.lower()
#     if "привет" in lower_msg:
#         # Если в тексте явно присутствует приветствие, но беседа уже идет, подкорректируем сообщение
#         bodies = (["Рад снова тебя видеть!", "Снова приветствую!", "Рад, что продолжаем общаться!"]
#                   if conv_context.strip() else [
#                       "Как здорово, что ты обратился ко мне.",
#                       "Рад слышать тебя! Надеюсь, у тебя отличное настроение.",
#                       "Приятно видеть такое тёплое приветствие."
#                   ])
#     elif "помог" in lower_msg or "задач" in lower_msg:
#         bodies = [
#             "Давай вместе разберёмся с этим вопросом.",
#             "Я с радостью помогу найти решение.",
#             "Расскажи, что именно тебя волнует."
#         ]
#     else:
#         bodies = [
#             "Мне интересно узнать, о чем ты думаешь, ведь каждый вопрос важен!",
#             "Никакие вопросы не бывают глупыми – я всегда рад помочь!",
#             "Расскажи подробнее, я с радостью отвечу на любой вопрос!"
#         ]
    
#     closings = [
#         "Буду рад помочь!", "Обращайся всегда!", "Давай двигаться дальше вместе."
#     ]
    
#     if greeting:
#         return f"{greeting} {random.choice(bodies)} {random.choice(closings)}"
#     else:
#         return f"{random.choice(bodies)} {random.choice(closings)}"

# def lookup_extended_info(user_message: str) -> str:
#     """
#     Ищет ключевые слова в сообщении и, при совпадениях, добавляет интересные факты из EXTENDED_RESPONSES.
#     """
#     lower_msg = user_message.lower()
#     info_list = []
#     for keyword, facts in EXTENDED_RESPONSES.items():
#         if keyword in lower_msg:
#             info_list.append(random.choice(facts))
#     if info_list:
#         return " Кстати, знаешь? " + " ".join(info_list)
#     return ""

# def generate_final_response(user_message: str, conv_context: str) -> str:
#     """
#     Объединяет динамичный ответ, анализ настроения и дополнительные факты.
#     """
#     base_response = generate_dynamic_response(user_message, conv_context)
#     extended_info = lookup_extended_info(user_message)
#     final_response = enrich_response_with_sentiment(base_response, user_message)
#     if extended_info:
#         final_response += extended_info
#     return final_response

# # --- СТАРЫЕ ФУНКЦИИ ГЕНЕРАЦИИ ОТВЕТОВ (сохраняем для совместимости) ---
# def generate_extended_response(text_segment: str, conv_context: str) -> str | None:
#     lower_text = text_segment.lower()
#     responses_found = []
#     for key, responses in EXTENDED_RESPONSES.items():
#         if key in lower_text:
#             responses_found.append(random.choice(responses))
#     if responses_found:
#         return " ".join(responses_found)
#     return None

# def generate_sentence_response(sentence: str, conv_context: str) -> str:
#     ext_response = generate_extended_response(sentence, conv_context)
#     if ext_response:
#         response = ext_response
#     else:
#         lower_sentence = sentence.lower()
#         if "привет" in lower_sentence:
#             response = random.choice(RESPONSES["привет"])
#         elif "как дел" in lower_sentence:
#             response = random.choice(RESPONSES["как дела"])
#         elif "как настроение" in lower_sentence:
#             response = random.choice(RESPONSES["как настроение"])
#         elif "пока" in lower_sentence:
#             response = random.choice(RESPONSES["пока"])
#         elif "не умею" in lower_sentence:
#             response = random.choice(RESPONSES["не умею"])
#         elif any(q in lower_sentence for q in ["почему", "зачем", "как"]) and conv_context:
#             response = "Интересный вопрос! Расскажи подробнее, чтобы я понял лучше. 🤓"
#         else:
#             tokenized = tokenizer(sentence)
#             _ = model(tokenized)
#             response = "Извини, я не совсем понял твой запрос. Можешь уточнить?"
#     enriched = response + " " + random.choice(["✨", "🔥", "💥", "🌟", "💫"])
#     return enrich_with_sentiment(enriched, sentence)

# def generate_combined_response(corrected_text: str, conv_context: str) -> str:
#     sentences = re.split(r'(?<=[.!?])\s+', corrected_text)
#     responses = []
#     for sentence in sentences:
#         if sentence.strip():
#             responses.append(generate_sentence_response(sentence, conv_context))
#     return " ".join(responses)

# def generate_response(corrected_text: str, conv_context: str) -> str:
#     combined = generate_combined_response(corrected_text, conv_context)
#     if combined and combined.strip():
#         return combined
#     return "Пожалуйста, уточни свой запрос."

# # --- ФУНКЦИЯ ИЗВЛЕЧЕНИЯ КОДА (если код в тройных обратных кавычках) ---
# def extract_code_snippet(text: str) -> str:
#     m = re.search(r"```(.*?)```", text, flags=re.DOTALL)
#     if m:
#         return m.group(1).strip()
#     return ""

# # --- РАБОТА С ИЗОБРАЖЕНИЯМИ ---
# def describe_image(image_path: str) -> str:
#     possible_descriptions = [
#         "это удивительное фото природы 🌳",
#         "здесь виден городской пейзаж 🏙️",
#         "на фото портрет интересного человека 😊",
#         "снимок с яркими красками 🎨",
#         "на фото что-то загадочное... 🤔"
#     ]
#     base = random.choice(possible_descriptions)
#     count = random.randint(1, 5)
#     return f"{base} и определено {count} объектов."

# def create_image(prompt: str) -> str:
#     """
#     Улучшенная генерация изображения: используется пастельный фон, аккуратное разбиение текста и добавление тени.
#     """
#     img_size = (512, 512)
#     bg_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
#     img = Image.new('RGB', img_size, color=bg_color)
#     draw = ImageDraw.Draw(img)
#     try:
#         font_size = 28
#         font = ImageFont.truetype("arial.ttf", font_size)
#     except IOError:
#         font = ImageFont.load_default()
    
#     max_width = img_size[0] - 40  # отступы по бокам
#     words = prompt.split()
#     lines = []
#     current_line = ""
#     for word in words:
#         test_line = f"{current_line} {word}".strip() if current_line else word
#         bbox = draw.textbbox((0, 0), test_line, font=font)
#         line_width = bbox[2] - bbox[0]
#         if line_width <= max_width:
#             current_line = test_line
#         else:
#             lines.append(current_line)
#             current_line = word
#     if current_line:
#         lines.append(current_line)
#     text = "\n".join(lines)
#     bbox = draw.multiline_textbbox((0, 0), text, font=font)
#     textwidth = bbox[2] - bbox[0]
#     textheight = bbox[3] - bbox[1]
#     position = ((img_size[0] - textwidth) / 2, (img_size[1] - textheight) / 2)
    
#     # Теневой эффект для улучшения читаемости текста
#     shadow_offset = 2
#     shadow_color = (0, 0, 0)
#     draw.multiline_text((position[0] + shadow_offset, position[1] + shadow_offset),
#                         text, font=font, fill=shadow_color, align="center")
#     draw.multiline_text(position, text, font=font, fill=(255, 255, 255), align="center")
    
#     filename = f"generated_{random.randint(1000,9999)}.jpg"
#     img.save(filename)
#     return filename

# # --- Респонсы для помощи с кодом ---
# CODE_HELP_RESPONSES = {
#     "python": "Пример на Python:\n```python\nprint('Hello, world!')\n```",
#     "telegram": ("Для создания Telegram-бота используй python-telegram-bot:\n"
#                  "```python\nfrom telegram import Update\nfrom telegram.ext import Application, CommandHandler\n# Твой код\n```"),
#     "сортировка": "Для сортировки списка используй sorted:\n```python\nmy_list = [3, 1, 2]\nsorted_list = sorted(my_list)\n```",
#     "функция": "Пример функции на Python:\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('World'))\n```",
#     "цикл": "Пример цикла for:\n```python\nfor i in range(5):\n    print(i)\n```",
#     "класс": "Пример определения класса:\n```python\nclass Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'Hello, my name is {self.name}')\n\np = Person('Alice')\np.greet()\n```",
#     "словарь": "Пример работы со словарями:\n```python\ndict_example = {'a': 1, 'b': 2}\nprint(dict_example['a'])\n```",
#     "json": "Пример работы с JSON:\n```python\nimport json\nsample = {'key': 'value'}\njson_str = json.dumps(sample)\nprint(json_str)\n```",
#     "sql": "Пример SQL-запроса с sqlite3:\n```python\nimport sqlite3\nconn = sqlite3.connect('example.db')\nc = conn.cursor()\nc.execute('SELECT * FROM table_name')\nrows = c.fetchall()\nprint(rows)\n```"
# }

# def get_code_help_response(query: str) -> str:
#     query_lower = query.lower()
#     for key, response in CODE_HELP_RESPONSES.items():
#         if key in query_lower:
#             return response
#     return "Извини, не нашёл подходящего примера. Попробуй уточнить запрос."

# def explain_code(code_snippet: str) -> str:
#     explanation = []
#     code_lower = code_snippet.lower()
#     if "def " in code_lower:
#         explanation.append("Этот фрагмент определяет функцию, которую можно вызывать многократно.")
#     if "for " in code_lower:
#         explanation.append("Цикл for используется для итерации по элементам.")
#     if "if " in code_lower:
#         explanation.append("Условный оператор выбирает ветку исполнения.")
#     if "class " in code_lower:
#         explanation.append("Определён класс — шаблон для создания объектов.")
#     if not explanation:
#         explanation.append("Фрагмент кода выглядит стандартно; попробуй добавить больше деталей.")
#     return " ".join(explanation)

# # --- Триггеры для различных запросов ---
# CODE_HELP_TRIGGERS = [
#     "помоги с кодом", "как сделать", "покажи пример", "дай подсказку по коду",
#     "подскажи код", "покажи подсказку по коду", "дай код", "помоги с программированием",
#     "код подсказка", "дай подсказку", "покажи подсказку", "подскажи пример", "дай подсказку по програмированию"
# ]

# IDEA_TRIGGERS = [
#     "дай идею", "идея для проекта", "предложи идею", "хочу идею"
# ]

# PHOTO_TRIGGERS = [
#     "сделай фото", "создай фото", "сгенерируй фотку", "сгенерируй фото",
#     "сделай фотку", "генерируй картинку", "создай изображение", "сделай изображение"
# ]

# # --- Обработчик текстовых сообщений ---
# async def handle_text_message(update: Update, context) -> None:
#     chat_id = update.effective_chat.id
#     user_input = update.message.text.strip()
    
#     # если пользователь ввел текст без пробелов – пытаемся исправить
#     user_input = fix_missing_spaces(user_input)
#     lower_input = user_input.lower()

#     # Если ранее задано действие (например, ожидание уточнения для фото)
#     if "action" in context.user_data:
#         action = context.user_data.pop("action")
#         if action == "create_photo":
#             prompt = user_input
#             filename = create_image(prompt)
#             with open(filename, "rb") as photo:
#                 await update.message.reply_photo(photo=photo, caption=f"Вот твоё фото: {prompt}")
#             os.remove(filename)
#             return

#     # Проверяем триггеры для создания фото
#     if any(trigger in lower_input for trigger in PHOTO_TRIGGERS):
#         await update.message.reply_text("Расскажи, какое фото ты хочешь создать?")
#         context.user_data["action"] = "create_photo"
#         return

#     # Если пользователь просит объяснить код
#     if any(trigger in lower_input for trigger in ["объясни код", "расскажи, что делает код", "разбери код", "поясни код"]):
#         code_snippet = extract_code_snippet(user_input)
#         if code_snippet:
#             explanation = explain_code(code_snippet)
#             await update.message.reply_text(explanation, parse_mode="Markdown")
#         else:
#             await update.message.reply_text("Я не вижу кода. Пришли код, заключённый в тройные обратные кавычки (```).")
#         return

#     # Если запрос на идею для проекта
#     if any(trigger in lower_input for trigger in IDEA_TRIGGERS):
#         idea = random.choice(IDEA_PROJECTS)
#         await update.message.reply_text(idea, parse_mode="Markdown")
#         return

#     # Если пользователь просит помощь с кодом
#     if any(trigger in lower_input for trigger in CODE_HELP_TRIGGERS):
#         response = get_code_help_response(user_input)
#         await update.message.reply_text(response, parse_mode="Markdown")
#         return

#     # Если обсуждается настроение
#     if "настроение" in lower_input:
#         await update.message.reply_text(random.choice(RESPONSES["как настроение"]))
#         return

#     # Стандартная обработка: корректируем текст, сохраняем историю и генерируем финальный ответ с учётом контекста
#     corrected = correct_text(user_input)
#     update_conversation(chat_id, corrected)
#     conv_context = get_context(chat_id)
#     logger.info(f"[Chat {chat_id}] Получено: {user_input} | Исправлено: {corrected}")
#     logger.info(f"[Chat {chat_id}] Контекст: {conv_context}")
    
#     response = generate_final_response(user_input, conv_context)
#     update_conversation(chat_id, response)
#     await update.message.reply_text(response)

# # --- Обработчик фотографий ---
# async def handle_photo_message(update: Update, context) -> None:
#     chat_id = update.effective_chat.id
#     if not update.message.photo:
#         return
#     photo_file = await update.message.photo[-1].get_file()
#     local_filename = f"temp_{chat_id}.jpg"
#     await photo_file.download_to_drive(custom_path=local_filename)
#     image_description = describe_image(local_filename)
#     os.remove(local_filename)
#     reply_text = f"Я проанализировал фото и вижу: {image_description}\nКак тебе такое?"
#     update_conversation(chat_id, reply_text)
#     await update.message.reply_text(reply_text)

# # --- Команда /start ---
# async def start_command(update: Update, context) -> None:
#     welcome = (
#         "Привет! Я начинающий ИИ, разработанный яйцом глеба, и постоянно развиваюсь. 😊\n\n"
#         "Я понимаю твои запросы на естественном языке – просто напиши, что тебе нужно.\n\n"
#         "Примеры:\n"
#         "• 'Сделай фото заката'\n"
#         "• 'Как сделать сортировку в Python?'\n"
#         "• 'Объясни код: ```python\nprint(\"Hello\")\n```'\n"
#         "• 'Дай идею для проекта'\n\n"
#         "Пиши без специальных команд – я всё понимаю!"
#     )
#     await update.message.reply_text(welcome, reply_markup=ReplyKeyboardRemove())

# # --- Основной запуск приложения ---
# async def main() -> None:
#     # app = Application.builder().token(BOT_TOKEN).build()
    
#     app.add_handler(CommandHandler("start", start_command))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
#     app.add_handler(MessageHandler(filters.PHOTO, handle_photo_message))
    
#     logger.info("Бот запущен и готов к живому диалогу! 🚀")
#     await app.run_polling()

# if __name__ == '__main__':
#     asyncio.run(main())
#     logger.info("Бот завершил работу. 👋")