from telegram import Update , InlineKeyboardMarkup , InlineKeyboardButton
from telegram.ext import CallbackContext

def welcome(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Hurmatli foydalanuvchi bizning botda yangimisiz!*" ,
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard = [
                [InlineKeyboardButton("Ha endi boshladim 🥰" , callback_data="xa")],
                [InlineKeyboardButton("Eskilardanman 😅" , callback_data="yoq")]
            ]
        )
    )
    
def welcome02(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Ro'yxatdan o'tishga hush kelibsiz!*",
        parse_mode = 'markdown'
    )    
    bot.send_message(
        chat_id = user.id ,
        text = "*Hurmatli foydalanuvchi bizning botda yangimisiz!*" ,
        parse_mode = "markdown",
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard = [
                [InlineKeyboardButton("Ha endi boshladim 🥰" , callback_data="xa")],
                [InlineKeyboardButton("Eskilardanman 😅" , callback_data="yoq")]
            ]
        )
    )

def register(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Yangi foydalanuvchi sifatida ro'yxatdan o'tish boshlandi!*",
        parse_mode = 'markdown'
    )
    
    bot.send_message(
        chat_id = user.id ,
        text = "*USERNAME* kiriting!",
        parse_mode = "markdown"
    )