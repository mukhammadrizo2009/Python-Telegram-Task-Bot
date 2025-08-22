from config import TOKEN
from telegram.ext import Updater ,CommandHandler,  MessageHandler



def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    
    
    
if __name__ == '__main__':
    main()