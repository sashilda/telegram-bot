from telegram.ext import Updater, CommandHandler , MessageHandler, Filters     
from os import environ
import pprint
import logging

logging.basicConfig(format='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')
telegram_logger = logging.getLogger("telegram")
telegram_logger.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)

# Run in cmd line "source secrets.txt" before running
API_KEY = environ.get('API_KEY') 

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    logger.debug(text)
    logging.info(text)
    # pprint method print a dictionary in a column
    pprint.pprint(update.to_dict())

    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    # print(user_text)
    logger.info(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(API_KEY)
    mydisp = mybot.dispatcher
    mydisp.add_handler(CommandHandler("start", greet_user))
    mydisp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       
main()       