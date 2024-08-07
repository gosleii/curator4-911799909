import telebot

bot = telebot.TeleBot("7450196470:AAE8pedJteZJQg5RddbRLw5hV63mY-oNFP8")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, милашка. Ты хочешь стать _моим новым маленьким помощником_? Что? *Главный маг*? Нет, это было очень давно, сейчас я обычный библиотекарь, хи-хи. Не волнуйся, дорогуша, я хорошо о тебе позабочусь.", parse_mode="Markdown")

@bot.message_handler(commands=["lisa"])
def lisa_handler(message):
    bot.send_message(message.chat.id, "[Обо мне](https://genshin-impact.fandom.com/ru/wiki/Лиза)", parse_mode="Markdown")

@bot.message_handler(commands=["work"])
def work_handler(message):
    bot.send_message(message.chat.id, "Присядь, *поболтаем*, а работа никуда не убежит.", parse_mode="Markdown")

@bot.message_handler(commands=["gid"])
def gid_handler(message):
    bot.send_message(message.chat.id, "[Гайд](https://www.youtube.com/watch?v=-Q9OByxPoRw&t=431s)", parse_mode="Markdown")

@bot.message_handler(commands=["manhua"])
def manhua_handler(message):
    bot.send_message(message.chat.id, "[Маньхуа](https://mangalib.me/genshin-impact?section=info)", parse_mode="Markdown")

@bot.message_handler(commands=["me"])
def me_handler(message):
    bot.send_message(message.chat.id, "[Да да я](https://ru.pinterest.com/pin/13933080088960771/)", parse_mode="Markdown")

@bot.message_handler(commands=["bb"])
def bb_handler(message):
    bot.send_message(message.chat.id, "*Пока-пока, милашка~*", parse_mode="Markdown")


bot.infinity_polling()