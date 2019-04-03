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
