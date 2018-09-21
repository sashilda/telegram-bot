from random import choice
# import logging
from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize
import settings

def get_user_emo(user_data):
    
    if 'emo' not in user_data:
        emo = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        user_data['emo'] = emo

    return user_data['emo']

def get_avatar(user_data):
    emo = get_user_emo(user_data)
    return emo

def get_keyboard():
    contact_button = KeyboardButton('Send contacts', request_contact=True)
    location_button = KeyboardButton('Send your location', request_location=True)

    my_keyboard = ReplyKeyboardMarkup([['Send cat','Change avatar'],
                                        [contact_button, location_button]])

    return my_keyboard