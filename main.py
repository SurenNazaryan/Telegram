import os
import random
from dotenv import load_dotenv
from pytimeparse import parse
import ptbot


def reply(chat_id, text):
    message_id = bot.send_message(chat_id, "Запускаю таймер...")
    time = parse(text)
    bot.create_countdown(
        time,
        notify,
        chat_id=chat_id,
        message_id=message_id,
        time=time
    )
    bot.create_timer(
        time,
        notifyy,
        chat_id=chat_id,
        message_id=message_id
    )


def notify(secs_left, chat_id, message_id, time):
    bot.update_message(
        chat_id,
        message_id,
        "Осталось {} секунд!\n{}".format(
            secs_left,
            render_progressbar(time, time - secs_left)
        )
    )


def notifyy(chat_id, message_id):
    bot.update_message(chat_id, message_id, "Время вышло!")


def render_progressbar(
        total,
        iteration,
        prefix='',
        suffix='',
        length=30,
        fill='█',
        zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply)
    bot.run_bot()
