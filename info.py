from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def info(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Bu dasturda siz o'zingiz qilmoqchi bo'lgan chaqiruv (chellege) larni yoki o'zingiz bajarishingiz kerak bo'lgan har kunlik ishlaringizni yaratishingiz mumkin!*",
        parse_mode = "markdown")
        
    bot.send_message(
        chat_id = user.id,
        text = "*Savol va takliflar uchun:* muhammadrizomirzaev671@gmail.com",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga qaytish!")],
                [KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def get_info(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "*Bu dasturda siz o'zingiz qilmoqchi bo'lgan chaqiruv (chellege) larni yoki o'zingiz bajarishingiz kerak bo'lgan har kunlik ishlaringizni yaratishingiz mumkin!*",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Tushunarli bo'ldi 🤩")],
                [KeyboardButton("Tushunolmadim!🤔")] 
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def didnotunderstand(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    
    bot.send_message(
        chat_id = user.id,
        text = "*👉 Bu dastur yordamida siz har kuni qilishingiz kerak bo'lgan ishlaringizni yoki o'zingiz xohlagan topshiriqlar (chaqiruv/challenge) ni yozib, tartibga solishingiz mumkin.*",
        parse_mode = 'markdown'
    )
    
    bot.send_message(
        chat_id = user.id,
        text = f"*Tushunarli bo'ldimi? {user.first_name}*",
        parse_mode = "markdown",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Ha tushunali bo'ldi!")],
                [KeyboardButton("Albatta tushundim!")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
