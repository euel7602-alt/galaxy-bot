import sys
import subprocess

try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])
    import telebot

from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "8662370948:AAFCtfSId3BwzUqJ1DpbC18h5U5x6xqZtPI"
WEB_APP_URL = "https://sparkly-douhua-b44b4b.netlify.app"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    btn_play = KeyboardButton("🎮 ቪአይፒ ጨዋታ", web_app=WebAppInfo(url=WEB_APP_URL))
    btn_bonus = KeyboardButton("🎁 ፕሮሞ ኮድ")
    btn_deposit = KeyboardButton("💰 ገንዘብ ለማድረግ")
    btn_withdraw = KeyboardButton("💳 ወጪ ለማድረግ")
    btn_rules = KeyboardButton("🔗 ጋበዝ & አግኝ")
    btn_account = KeyboardButton("👤 ፕሮפይል & ሒሳብ")
    btn_help = KeyboardButton("🆘 እርዳታ")
    btn_lang = KeyboardButton("🌐 ቋንቋ / Language")
    
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

print("ቦቱ በመሥራት ላይ ነው...")
bot.polling()
