import psycopg2
from telegram import Update , InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardRemove
from telegram.ext import CallbackContext
import config

connection = psycopg2.connect(
    host=config.HOST,
    port=int(config.PORT),
    user=config.USER,
    password=config.PASSWORD,
    dbname=config.DBNAME
)

cursor = connection.cursor()


def start(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    cursor.execute(
        "INSERT INTO users (telegram_id, first_name) VALUES (%s, %s) ON CONFLICT (telegram_id) DO NOTHING",
        (user.id, user.first_name)
    )
    connection.commit()
    
    bot.send_message(
    chat_id=user.id,
    text=f"Assalomu alaykum *{user.first_name}*! _Bizning botga hush kelibsiz!_",
    parse_mode="Markdown"
)

    
    bot.send_message(
        chat_id = user.id,
        text = "Bizning BOT haqida ma'lumotga egamisiz?",
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard = [
                [InlineKeyboardButton("Albatta 🥰" , callback_data="ha")],
                [InlineKeyboardButton("Afsuski yo'q 😅" , callback_data="yo'q")]
            ]
        )
    )
    
def stop(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id=user.id,
        text="Dastur yakunlandi!😑",
        reply_markup=ReplyKeyboardRemove()
    )