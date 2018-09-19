from telegram.ext import Updater, CommandHandler , MessageHandler, Filters     
from os import environ
import pprint
import logging
import ephem
import inspect

planet_names = [s for s in dir(ephem)
                if s != "Planet" and not s.endswith("Body") 
                and inspect.isclass(getattr(ephem, s)) 
                and issubclass(getattr(ephem, s), ephem.Planet)]


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

def ephem_planet(bot, update):

    text = update.message.text  
    msg = "ephem_planet: {}".format(text)
    logger.debug(msg)
    wrds = text.split(' ')

    planet_found = None

    for w in wrds:
        if w in planet_names:
            planet_found = w
            break
    
    if planet_found:
        reply = "Planet {} found".format(planet_found)
    else:
        reply = "Planet not found"

    update.message.reply_text(reply)


def main():
    mybot = Updater(API_KEY)
    mydisp = mybot.dispatcher
    mydisp.add_handler(CommandHandler("start", greet_user))
    mydisp.add_handler(CommandHandler("ephem", ephem_planet))

    mydisp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()
       
main()       