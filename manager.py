from config import TOKEN
from telegram.ext import Updater , CommandHandler , CallbackQueryHandler , MessageHandler , Filters
from commands import start , stop
from info import info
from menu import menu


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    #CommandHandler
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("info" , info))
    dispatcher.add_handler(CommandHandler("stop" , stop))
    
    #InlineKeyboardCommand
    dispatcher.add_handler(CallbackQueryHandler(info , pattern="yo'q"))
    
    #MessengeHandler
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni to'xtatish!🤔") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Tushunarli bo'ldi 🤩") , menu))
    
    
    
    updater.start_polling()
    updater.idle()
    
    
    
if __name__ == '__main__':
    main()