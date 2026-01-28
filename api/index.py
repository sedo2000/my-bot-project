import os
import telebot
from flask import Flask, request, send_from_directory

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# الحصول على المسار الصحيح للمجلد الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. لعرض ملف الـ HTML عند فتح الرابط
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

# 2. لمعالجة رسائل تليجرام (الويب هوك)
@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

# مثال بسيط لأمر يعمل في البوت
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً! أنا أعمل الآن من Vercel.")
