import os
import telebot
from flask import Flask, request

TOKEN = "8494556301:AAEL3KLQMh3K318-Rtj1aCXr6Td4IKWMWIY" # ضعه مباشرة هنا للتجربة فقط
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Server is Running!</h1>"

# هذه الدالة هي المسؤولة عن الرد في تليجرام
@app.route('/', methods=['POST'])
def getMessage():
    try:
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "!", 200
    except Exception as e:
        return str(e), 500

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "شغال يمعود! لا تعصب")

# تأكد أنك حذفت bot.polling() تماماً
