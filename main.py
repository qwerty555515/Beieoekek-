import requests
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

SIGNS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for sign in SIGNS:
        markup.add(sign.capitalize())
    bot.send_message(message.chat.id, "Привет! Выбери свой знак зодиака:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() in SIGNS)
def get_horoscope(message):
    sign = message.text.lower()
    url = f"https://aztro.sameerkumar.website/?sign={sign}&day=today"
    response = requests.post(url)
    data = response.json()
    bot.send_message(message.chat.id, f"🔮 Гороскоп для {sign.capitalize()} на сегодня:\n\n{data['description']}")

bot.infinity_polling()
