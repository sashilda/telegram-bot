import datetime
import logging

import ephem
from utils import get_keyboard
logger = logging.getLogger(__name__)

planet_names = [p[2] for p in ephem._libastro.builtin_planets()[:8]]

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

    update.message.reply_text(reply,
                                reply_markup=get_keyboard())
