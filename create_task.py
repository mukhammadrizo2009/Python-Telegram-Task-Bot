from telegram import Update
from telegram.ext import CallbackContext

def create_task(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Task yaratishingiz mumkin!",
            
        
    )