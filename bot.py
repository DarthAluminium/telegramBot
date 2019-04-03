'''import requests
import telebot
import re
import token

WEEK_DAYS = ('ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ')
HASHTAG_VALIDATOR = re.compile(r"\s*(#([a-zA-Z0-9А-я]+)(?:_(\w+))?)\s*$")
# [1]: весь хештег без пробелов     [2]: первое слово до "_"     [3]: все слова после "_"


bot = telebot.TeleBot(token.BOT_TOKEN)


def format_message(text):
    lines = text.split('\n')
    day = lines[0].rstrip().lstrip()
    if day.upper() in WEEK_DAYS:
        del lines[0]
        return "📝 **{}**\n".format(day.capitalize()) + '\n'.join(['🖊 ' + s for s in lines]) + '\n#расписание'

    m = HASHTAG_VALIDATOR.match(lines[-1])
    if m is None:
        return None  # Нечего менять и редактировать

    if m[2].upper() == 'НОВОСТИ' and m[3] is None:
        del lines[-1]
        return "📰 **Новости:**\n" + '\n'.join(['➕ ' + s for s in lines]) + '\n' + m[1]

    if m[2] == 'англ':
        first_name = 'Английский язык'
    elif m[2] == 'ОБЖ':
        first_name = 'ОБЖ'
    else:
        first_name = m[2].capitalize()

    second_name = '' if m[3] is None else ' (%s)' % m[3]
    first_line = "📓 **{}{}:**\n".format(first_name, second_name)
    lines.pop()
    return first_line + '\n'.join(['🖊 ' + s for s in lines]) + '\n' + m[1]


@bot.message_handler(func = lambda msg: True)
@bot.edited_message_handler()
def format_hw_msg_all(msg):
    if message.chat.type == "channel":
        f_text = format_message(msg.text)
        if f_text:
	      bot.edit_message_text(f_text, parse_mode = 'Markdown')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?"
if name == 'main':
    bot.polling(none_stop=True)'''
import requests
import datetime
import token
import telebot

class Msk(datetime.tzinfo):
    def utcoffset(self, dt):
      return datetime.timedelta(hours=+3)

    def dst(self, dt):
        return datetime.timedelta(0)

bot = telebot.TeleBot(token.BOT_TOKEN)

def sleep(h, m, s):
    try:
        hour_start = datetime.datetime.now(Msk()).hour
        minute_start = datetime.datetime.now(Msk()).minute
        second_start = datetime.datetime.now(Msk()).second
        hour_stop = 0
        minute_stop = 0
        second_stop = 0
        while((hour_start+int(h) != hour_stop) or int(h) == 0):
            while(minute_start+int(m) != minute_stop or int(m) == 0):
                while(int(second_start+int(s)) != int(second_stop)):
                    hour_stop = datetime.datetime.now(Msk()).hour
                    minute_stop = datetime.datetime.now(Msk()).minute
                    second_stop = datetime.datetime.now(Msk()).second
                if int(m) == 0:
                    break
            if int(h) == 0:
                break
        return 'Stop'
    except TypeError:
        return 'Error'
        



@bot.message_handler(content_types=["text"])
def timer(message):
    bot.send_message(message.chat.id, 'Start')
    try:
        time = message.text.split()
        bot.send_message(message.chat.id, sleep(time[0], time[1], time[2]))
    except IndexError:
        bot.send_message(message.chat.id, 'Это самодельный таймер, бот вопринимает только строки в формате h m s, где h это часы m минуты, а s секунды')
    


if __name__ == '__main__':
    bot.polling(none_stop=True)
