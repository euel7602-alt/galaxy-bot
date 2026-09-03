import os
from flask import Flask
import telebot
from telebot import types

# ትክክለኛው የ Galaxy Bet ቦት ቶከን
TOKEN = "8662370948:AAFCTfSl3BwZUqJ1DpbC18h5U5x6xqZtPI"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # አዝራሮችን መፍጠር (Deposit, Withdraw, Play Game)
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # 1. ፕሌይ ጌም (Mini App) አዝራር - የራስህን ሚኒ አፕ ሊንክ እዚህ ከተረከብን በኋላ መቀየር ትችላለህ
    web_app = types.WebAppInfo(url="https://your-mini-app-url.com") 
    btn_play = types.InlineKeyboardButton("🎮 Play Game", web_app=web_app)
    
    # 2. ዲፖዚት አዝራር
    btn_deposit = types.InlineKeyboardButton("💳 Deposit", callback_data="deposit")
    
    # 3. ዊዝድሮ አዝራር
    btn_withdraw = types.InlineKeyboardButton("💰 Withdraw", callback_data="withdraw")
    
    markup.add(btn_play, btn_deposit, btn_withdraw)
    
    bot.send_message(
        message.chat.id, 
        "Welcome to *Galaxy Bet*! 🚀\n\nChoose an option below:", 
        parse_mode="Markdown", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "deposit":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "💳 To Deposit, please choose your payment method or contact support.")
    elif call.data == "withdraw":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "💰 To Withdraw, please enter your amount.")

# ቦቱን እና ሰርቨሩን ማስጀመር
if __name__ == "__main__":
    import threading
    def run_bot():
        bot.infinity_polling()
    
    t = threading.Thread(target=run_bot)
    t.start()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
