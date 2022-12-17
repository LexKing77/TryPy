import telebot

TOKEN = "5863966426:AAHyn1waL4OJoN2REAU2bg4OsB8JYYND00A"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
