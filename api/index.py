import os
import telebot
from flask import Flask, request

# جلب التوكن
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN) if TOKEN else None
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>البوت يعمل!</h1><p>إذا كنت ترى هذه الرسالة، فالكود سليم والمشكلة كانت في ملف HTML فقط.</p>"

@app.route('/', methods=['POST'])
def webhook():
    if bot and request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "OK", 200

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "وصلت رسالتك!")
