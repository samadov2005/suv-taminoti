from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# Joylashuv tugmasi
userButton = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    one_time_keyboard=True
)
userButton.add(KeyboardButton("sozlamalar"))
userButton.add(KeyboardButton("suv holati"))