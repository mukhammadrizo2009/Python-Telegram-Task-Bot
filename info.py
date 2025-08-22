from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def info(update: Update , context: CallbackContext) -> None:
    
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Bu dasturda siz o'zingiz qilmoqchi bo'lgan chaqiruv (chellege) larni yoki o'zingiz bajarishingiz kerak bo'lgan har kunlik ishlaringizni yaratishingiz mumkin!*",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Tushunarli bo'ldi 🤩")],
                [KeyboardButton("Dasturni to'xtatish!🤔")] 
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    ) 