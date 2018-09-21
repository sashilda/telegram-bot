import logging
from glob import glob
from random import choice
from utils import get_keyboard

logger = logging.getLogger(__name__)

def send_cat_picture(bot, update, user_data):
    cat_list = glob('Images/*cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'),
                                reply_markup=get_keyboard())