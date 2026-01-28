from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import telebot
import os

app = FastAPI()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# هذا المسار سيعرض ملف HTML عند فتح الرابط في المتصفح
@app.get("/")
async def read_index():
    # نحدد مسار الملف (يفترض أنه في نفس المجلد)
    path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(path)

# هذا المسار يستقبل رسائل تليجرام (الويب هوك)
@app.post("/")
async def telegram_webhook(request: Request):
    json_str = await request.body()
    update = telebot.types.Update.de_json(json_str.decode("utf-8"))
    bot.process_new_updates([update])
    return {"status": "ok"}
