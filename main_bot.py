import logging

from telegram.ext import Updater, CommandHandler , MessageHandler, RegexHandler, Filters 

from common_handlers import greet_user, talk_to_me, change_avatar
from cat_handlers import send_cat_picture
from ephem_handlers import ephem_planet
from personal_info_handlers import get_contact, get_location
from settings import API_KEY 


def start_bot():
    mybot = Updater(API_KEY)#(API_KEY)
    mydisp = mybot.dispatcher

    # common command handler
    mydisp.add_handler(CommandHandler(["start", "hello"], greet_user, pass_user_data=True))
    
    # ephem specific handler
    mydisp.add_handler(CommandHandler("planet", ephem_planet, pass_user_data=True))

    # cat-bot specific handler
    mydisp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))

    # cat-bot specific handler
    mydisp.add_handler(RegexHandler('^(Send cat)$', send_cat_picture, pass_user_data=True))

    # common command handler
    mydisp.add_handler(RegexHandler('^(Change avatar)$', change_avatar, pass_user_data=True))

    # personal info handler
    mydisp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))

    # personal info handler
    mydisp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))

    # common free text handler
    mydisp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()

if __name__== '__main__':
    logging.basicConfig(format='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')
    telegram_logger = logging.getLogger("telegram")
    telegram_logger.setLevel(logging.INFO)

    start_bot()  