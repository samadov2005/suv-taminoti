from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Joylashuv tugmasi
location_button = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    one_time_keyboard=True
)
location_button.add(KeyboardButton("Joylashuvni yuborish 📍", request_location=True))