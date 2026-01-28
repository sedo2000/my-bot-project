import os
import telebot
from flask import Flask, request, send_from_directory

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# تحديد مسار المجلد الحالي بدقة
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    # محاولة عرض الملف، وإذا فشل يعطي رسالة واضحة بدلاً من الانهيار
    try:
        return send_from_directory(BASE_DIR, 'index.html')
    except:
        return "تم تشغيل المحرك، لكن ملف index.html غير موجود في مجلد api/"

@app.route('/', methods=['POST'])
def telegram_webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

# تأكد من عدم وجود bot.polling() في نهاية الملف
