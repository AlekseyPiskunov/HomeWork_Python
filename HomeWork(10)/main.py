from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from credits import bot_token

from module_weather import *
from datetime import datetime
from spy import *

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Создаём текущее время
def create_time():
    time = datetime.now().strftime('%H:%M')
    return time
# Создаём текущую дату
def create_data():
    current_date = datetime.now().date()
    return current_date


def start(update, context):
    keyboard = [
        [InlineKeyboardButton('Время', callback_data='1'), InlineKeyboardButton('Дата', callback_data='2')],
        [InlineKeyboardButton('Погода в Москве', callback_data='3')],
        [InlineKeyboardButton('Погода в Санкт-Петербурге', callback_data='4')]
    ]
    update.message.reply_text('Выбирай:', reply_markup=InlineKeyboardMarkup(keyboard))

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.bot.send_message(update.effective_chat.id, f'Точное время - {create_time()}')
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, f'Дата: {create_data()}')
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, f'В Москве: {create_weather_moscow()[0]}c\n{create_weather_moscow()[1]}\nСостояние: {create_weather_moscow()[2]}')
    elif query.data == '4':
        context.bot.send_message(update.effective_chat.id, f'В Санкт-Петербурге: {create_weather_st_petersburg()[0]}\N{DEGREE SIGN}c\n{create_weather_st_petersburg()[1]}\N{DEGREE SIGN}c\nСостояние: {create_weather_st_petersburg()[2]}')

def unknow(update, context):
    context.bot.send_message(update.effective_chat.id, 'Такой команды нету!\nЕсть только: /start')

def message(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, f'Я не общаюсь, {update.effective_user.first_name}!\nПопробуй команду: /start')


button_handler = CallbackQueryHandler(button)
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, message)
unknow_handler = MessageHandler(Filters.command, unknow)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(unknow_handler)
dispatcher.add_handler(message_handler)

print('start server')
updater.start_polling()
updater.idle()