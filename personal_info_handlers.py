from utils import get_avatar, get_keyboard

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Thanks for your contact {}'.format(get_avatar(user_data)),
                                reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Thanks for your location {}'.format(get_avatar(user_data)),
                                reply_markup=get_keyboard())
