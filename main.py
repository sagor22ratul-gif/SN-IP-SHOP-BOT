import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row(KeyboardButton("🆔 IP কিনুন"), KeyboardButton("🔐 VPN কিনুন"))
    menu.row(KeyboardButton("💎 ডিপোজিট"), KeyboardButton("💰 আমার ব্যালেন্স"))
    menu.row(KeyboardButton("📦 আমার অর্ডার"), KeyboardButton("📘 টিউটোরিয়াল"))
    menu.row(KeyboardButton("🎧 সাপোর্ট"), KeyboardButton("🌐 ভাষা"))

    bot.send_message(
        message.chat.id,
        "💎 স্বাগতম Number Coding Bot-এ!\n\n"
        "নিচের মেনু থেকে একটি অপশন বেছে নিন।\n"
        "💰 অনলাইন আয়ের সুযোগ ও কাজের নিয়ম জানতে সেবাসমূহ দেখুন।\n"
        "⚠️ আয় নিশ্চিত নয়; কাজ ও যোগ্যতার ওপর নির্ভরশীল।",
        reply_markup=menu
    )

@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    responses = {
        "🆔 IP কিনুন": "🆔 IP সেবার বিস্তারিত জানতে সাপোর্টে যোগাযোগ করুন।",
        "🔐 VPN কিনুন": "🔐 VPN সেবার বিস্তারিত জানতে সাপোর্টে যোগাযোগ করুন।",
        "💎 ডিপোজিট": "💳 ডিপোজিটের নিয়ম জানতে অ্যাডমিনের সঙ্গে যোগাযোগ করুন।",
        "💰 আমার ব্যালেন্স": "💰 ব্যালেন্স দেখতে হলে অ্যাকাউন্ট ব্যবস্থা যুক্ত করতে হবে।",
        "📦 আমার অর্ডার": "📦 অর্ডার ব্যবস্থাটি শিগগির যুক্ত করা হবে।",
        "📘 টিউটোরিয়াল": "📘 টিউটোরিয়াল পেতে অ্যাডমিনের সঙ্গে যোগাযোগ করুন।",
        "🎧 সাপোর্ট": "🎧 সাপোর্টের জন্য অ্যাডমিনকে মেসেজ করুন।",
        "🌐 ভাষা": "🌐 বাংলা ভাষা নির্বাচিত আছে।"
    }
    bot.reply_to(message, responses.get(message.text, "মেনু থেকে একটি অপশন বেছে নিন।"))

if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN সেট করা নেই।")
    bot.infinity_polling()
