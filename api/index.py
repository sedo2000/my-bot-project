import os
import telebot
from flask import Flask, request, send_from_directory

# 1. إعداد البوت والتوكن
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 2. مسار لعرض ملف الـ HTML الخاص بك
@app.route('/')
def serve_index():
    # يفترض أن ملف index.html موجود في نفس المجلد
    return send_from_directory(os.path.dirname(__file__), 'index.html')

# 3. مسار الـ Webhook الخاص بتليجرام
@app.route('/', methods=['POST'])
def telegram_webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Invalid Request", 403

# 4. معالجة أوامر البوت
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "تم استقبال طلبك والبوت يعمل!")

# ملاحظة: لا تضع bot.polling() هنا أبداً
