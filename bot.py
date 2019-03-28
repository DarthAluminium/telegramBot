import telebot
import re

WEEK_DAYS = ('ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ')
HASHTAG_VALIDATOR = re.compile(r"\s*(#([a-zA-Z0-9А-я]+)(?:_(\w+))?)\s*$")
# [1]: весь хештег без пробелов     [2]: первое слово до "_"     [3]: все слова после "_"


bot = telebot.TeleBot(BOT_TOKEN)


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
bot.polling()
