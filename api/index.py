import os
import telebot
from flask import Flask, request, send_from_directory

# إعدادات البوت
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# الحصول على المسار الحالي للمجلد
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # التأكد من إرسال ملف index.html الخاص بك
    try:
        return send_from_directory(BASE_DIR, 'index.html')
    except Exception as e:
        return f"File index.html not found! Error: {str(e)}", 404

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

# أضف أوامر البوت هنا
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "تم تفعيل البوت بنجاح!")
