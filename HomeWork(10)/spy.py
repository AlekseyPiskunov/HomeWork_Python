from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    with open('db.txt', 'a', encoding='utf-8') as file:
        file.write(f'Имя: {update.effective_user.first_name}, id: {update.effective_user.id}, Сообщение: {update.message.text}\n')

