from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext


def menu(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Sahifalar ro'yhati ochilidi!😉 \
            Sahifalardan birini tanalashingiz mumkin!📱*",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton("Tasklardan o'chirish!") , KeyboardButton("Tasklar ro'yhatini ko'rish!")],
                 [KeyboardButton("Task yaratish!")],
                [KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def back_to_menu(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Sahifalar ro'yhatiga qaytildi!*",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton("Task yaratish!") , KeyboardButton("Taskni bajarildi qilish!")],
                [KeyboardButton("Tasklardan o'chirish!") , KeyboardButton("Tasklar ro'yhatini ko'rish!")],
                [KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )