from telegram import Update
from telegram.ext import CallbackContext


def login(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Iltimos ro'yxatdan o'tgan USERNAME-ni kiriting!*",
        parse_mode = "markdown"
    )