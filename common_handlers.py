from random import choice
import logging

from emoji import emojize

import settings

logger = logging.getLogger(__name__)

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