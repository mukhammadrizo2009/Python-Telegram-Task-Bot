from config import TOKEN
from telegram.ext import Updater , CommandHandler , CallbackQueryHandler , MessageHandler , Filters
from commands import start , stop
from info import get_info , didnotunderstand , info
from menu import menu
from login import login
from register import register , welcome02 , welcome


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    #CommandHandler
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("info" , info))
    dispatcher.add_handler(CommandHandler("stop" , stop))
    
    #InlineKeyboardCommand
    dispatcher.add_handler(CallbackQueryHandler(get_info , pattern="yo'q"))
    dispatcher.add_handler(CallbackQueryHandler(welcome02 , pattern="ha"))
    dispatcher.add_handler(CallbackQueryHandler(login , pattern="yoq"))
    dispatcher.add_handler(CallbackQueryHandler(register , pattern='xa'))
    
    #MessengeHandler
    dispatcher.add_handler(MessageHandler(Filters.text("Tushunarli bo'ldi 🤩") , welcome))
    dispatcher.add_handler(MessageHandler(Filters.text("Tushunolmadim!🤔") , didnotunderstand))
    dispatcher.add_handler(MessageHandler(Filters.text("Ha tushunali bo'ldi!") , welcome))
    dispatcher.add_handler(MessageHandler(Filters.text("Albatta tushundim!") , welcome))
    
    updater.start_polling()
    updater.idle()
    
    
    
if __name__ == '__main__':
    main()