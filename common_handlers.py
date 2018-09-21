from random import choice
import logging
from telegram import ReplyKeyboardMarkup, KeyboardButton

from emoji import emojize

import settings
from utils import get_user_emo, get_keyboard


logger = logging.getLogger(__name__)

def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)

    text = 'Hello! {}'.format(emo)

    # contact_button = KeyboardButton('Send contacts', request_contact=True)
    # location_button = KeyboardButton('Send your location', request_location=True)

    # my_keyboard = ReplyKeyboardMarkup([['Send cat','Change avatar'],
    #                                     [contact_button, location_button]])
    
    # logging.info(pprint.pformat(update.to_dict()))
    # pprint method print a dictionary in a column
    update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(bot, update, user_data):
    user_text = "Hello {}{}! You wrote: {}".format(update.message.chat.first_name,
                                                   user_data['emo'],
                                                   update.message.text) 
    # print(user_text)
    logger.info(user_text)
    update.message.reply_text(user_text,
                                reply_markup=get_keyboard())    

def change_avatar(bot, update, user_data):
    # if 'emo' in user_data:
    #     del user_data['emo']
    user_data.pop('emo', None)
    emo = get_user_emo(user_data)
    update.message.reply_text("Avatar has changed! {}".format(emo),
                                reply_markup=get_keyboard())
