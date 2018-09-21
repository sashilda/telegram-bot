from telegram.ext import Updater, CommandHandler , MessageHandler, Filters 

from glob import glob
from emoji import emojize
from os import environ
from random import choice


import pprint
import logging
import ephem
import inspect
import datetime
import settings

# planet_names = [s for s in dir(ephem)
#                 if s != "Planet" and not s.endswith("Body") 
#                 and inspect.isclass(getattr(ephem, s)) 
#                 and issubclass(getattr(ephem, s), ephem.Planet)]
planet_names = [p[2] for p in ephem._libastro.builtin_planets()[:8]]


logging.basicConfig(format='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')
telegram_logger = logging.getLogger("telegram")
telegram_logger.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
#ch = logging.StreamHandler()
#logger.addHandler(ch)

# Run in cmd line "source secrets.txt" before running
API_KEY = environ.get('API_KEY') 

#USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

def greet_user(bot, update, user_data):
    emo = emojize(choice(settings.USER_EMOJI), use_aliases=True)
    user_data['emo'] = emo

    text = 'Hello! {}'.format(emo)
    
    # logging.info(pprint.pformat(update.to_dict()))
    # pprint method print a dictionary in a column
    update.message.reply_text(text)

def talk_to_me(bot, update, user_data):
    user_text = "Hello {}{}! You wrote: {}".format(update.message.chat.first_name,
                                                   user_data['emo'],
                                                   update.message.text) 
    # print(user_text)
    logger.info(user_text)
    update.message.reply_text(user_text)

def ephem_planet(bot, update, user_data):

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
        planet_class = getattr(ephem, planet_found)
        today = datetime.datetime.today().strftime('%Y/%m/%d') #'2018/09/19'
        planet = planet_class(today)
        constellation = ephem.constellation(planet)[1]
        reply = "{} now in {}".format(planet_found, constellation)
    else:
        reply = "Planet not found"

    update.message.reply_text(reply)

def send_cat_picture(bot, update, user_data):
    cat_list = glob('Images/*cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))

def main():
    mybot = Updater("688721336:AAFy8ftMA6UZlFumVUSncQGMm79NAuHGJbA")#(API_KEY)
    mydisp = mybot.dispatcher
    mydisp.add_handler(CommandHandler(["start", "hello"], greet_user, pass_user_data=True))
    mydisp.add_handler(CommandHandler("planet", ephem_planet, pass_user_data=True))
    mydisp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))

    mydisp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))


    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
     logging.basicConfig(format='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')
    telegram_logger = logging.getLogger("telegram")
    telegram_logger.setLevel(logging.INFO)
    main()       