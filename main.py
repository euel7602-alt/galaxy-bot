import os
import telebot
from flask import Flask
from threading import Thread

TOKEN = "8662370948:AAFCtfSId3BwzUqJ1DpbC18h5U5x6xqZtPI"
WEB_APP_URL = "https://sparkly-douhua-b44b4b.netlify.app"

bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Galaxy Bot is alive!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_play = telebot.types.KeyboardButton("🎮 ቪአይፒ ጨዋታ", web_app=telebot.types.WebAppInfo(url=WEB_APP_URL))
    btn_bonus = telebot.types.KeyboardButton("🎁 ፕሮሞ ኮድ")
    btn_deposit = telebot.types.KeyboardButton("💰 ገንዘብ ለማድረግ")
    btn_withdraw = telebot.types.KeyboardButton("💳 ወጪ ለማድረግ")
    btn_rules = telebot.types.KeyboardButton("🔗 ጋበዝ & አግኝ")
    btn_account = telebot.types.KeyboardButton("👤 ፕሮפይል & ሒሳብ")
    btn_help = telebot.types.KeyboardButton("🆘 እርዳታ")
    btn_lang = telebot.types.KeyboardButton("🌐 ቋንቋ / Language")
    
    markup.add(btn_play, btn_bonus)
    markup.add(btn_deposit, btn_withdraw)
    markup.add(btn_rules, btn_account)
    markup.add(btn_help, btn_lang)
    
    welcome_text = (
        f"እንኳን ወደ ጋላክሲ ቤቲንግ በሰላም መጡ! 🎰\n\n"
        f"ሰላም {user_name}!\n"
        f"የጨዋታ ሒሳብ: 0.00 ETB\n"
        f"የሽልማት ሒሳብ: 0.00 ETB\n\n"
        f"ከታች ያሉትን ቁልፎች በመጠቀም አገልግሎቶቻችንን ያግኙ 👇"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

if __name__ == "__main__":
    t = Thread(target=run_web)
    t.start()
    
    print("ቦቱ እና ዌብሰርቨሩ በመሥራት ላይ ናቸው...")
    bot.infinity_polling()
