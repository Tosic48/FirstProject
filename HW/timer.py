#When you press the "Reset" button, we reset the timer.
from datetime import datetime
import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

start_time = None

@bot.message_handler(commands=['start'])
def start(message):
    global start_time
    start_time = datetime.now()
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Start', 'Stop', 'Reset']])
    bot.send_message(message.chat.id, 'Press the button to start the timer:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Start')
def start_timer(message):
    global start_time
    start_time = datetime.now()
    bot.send_message(message.chat.id, 'Timer started at {}'.format(start_time))

@bot.message_handler(func=lambda message: message.text == 'Stop')
def stop_timer(message):
    global start_time
    if start_time is None:
        bot.send_message(message.chat.id, 'Timer not started yet')
    else:
        elapsed_time = datetime.now() - start_time
        bot.send_message(message.chat.id, 'Time elapsed: {} seconds'.format(elapsed_time))

@bot.message_handler(func=lambda message: message.text == 'Reset')
def reset_timer(message):
    global start_time
    start_time = None
    bot.send_message(message.chat.id, 'Timer reset')

bot.polling()