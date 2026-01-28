import os
from flask import Flask, request, send_from_directory
import telebot

# إعدادات البوت - التوكن مباشرة لضمان العمل
TOKEN = "8494556301:AAEL3KLQMh3K318-Rtj1aCXr6Td4IKWMWIY"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# تحديد مسار المجلد الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # محاولة عرض ملف HTML، وإذا لم يوجد يعرض رسالة نصية
    try:
        return send_from_directory(BASE_DIR, 'index.html')
    except:
        return "<h1>Server is running!</h1><p>But index.html was not found in api/ folder.</p>"

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تم استقبال رسالتك بنجاح!")
