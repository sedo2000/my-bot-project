import os
import telebot
from flask import Flask, request, send_from_directory

# محاولة جلب التوكن
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN) if TOKEN else None
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    # فحص التوكن أولاً
    if not TOKEN:
        return "خطأ: لم يتم العثور على TELEGRAM_BOT_TOKEN في إعدادات Vercel", 500
    
    # محاولة عرض الملف
    html_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(html_path):
        return send_from_directory(BASE_DIR, 'index.html')
    else:
        return f"السيرفر يعمل، لكن ملف index.html غير موجود في هذا المسار: {html_path}", 404

@app.route('/', methods=['POST'])
def webhook():
    if bot and request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Status: Active", 200

# أوامر البوت
if bot:
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message, "أهلاً بك! البوت يعمل بنجاح.")
