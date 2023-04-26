import os
import telebot
import openai

BOT_TOKEN = os.environ.get('BOT_TOKEN')
openai.api_key = os.environ.get('OPEN_API')

BOT_HANDLE = '@the_nenuco_bot'
BOT_PERSONALITY = 'Responde de manera sarcastica, '
MODEL = 'gpt-3.5-turbo'

bot = telebot.TeleBot(BOT_TOKEN)

# Contexto del asistente
context = {"role": "system",
            "content": "Eres un asistente muy sarcastico."}
messages = [context]

# Let's define a message handler that handles incoming /start and /hello commands.
# @bot.message_handler(commands=['nenu'])
@bot.message_handler(func=lambda message: 'epa' in message.text.lower())
def send_welcome(message):
    bot.reply_to(message, "Khe paz0 Zhiamoooooooooooooooo")

# Define una función para manejar los mensajes entrantes
@bot.message_handler(func=lambda message: BOT_HANDLE in message.text.lower())
def handle_mentions(message):
    # Envía una respuesta al usuario que mencionó al bot
    bot.reply_to(message, 'hablame perry')

bot.infinity_polling()

