import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")
print("TOKEN LIDO:", repr(TOKEN))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot funcionando!")

print("Bot polling started")
bot.polling()
