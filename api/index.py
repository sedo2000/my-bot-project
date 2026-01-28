import os
from flask import Flask, request
import telebot

# ضع التوكن هنا مباشرة للتجربة لضمان عدم وجود خطأ في المتغيرات البيئية
TOKEN = "8494556301:AAEL3KLQMh3K318-Rtj1aCXr6Td4IKWMWIY"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "The server is finally alive!"

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    return "!", 200

@bot.message_handler(func=lambda m: True)
def reply(message):
    bot.reply_to(message, "أهلاً! أنا أسمعك الآن بوضوح.")
