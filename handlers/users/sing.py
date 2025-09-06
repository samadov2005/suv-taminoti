from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart,Command

from loader import dp
from states.personalData import PersonalData
from keyboards.default.location_buttons import location_button
from keyboards.default.users_button import userButton

# /start komandasi
@dp.message_handler(CommandStart())
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting")
    await PersonalData.fullName.set()


# Ismni qabul qilish
@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"name": fullname})
    await message.answer("Telefon raqamingizni kiriting:")
    await PersonalData.next()


# Telefon raqamini qabul qilish
@dp.message_handler(state=PersonalData.phonenumber)
async def answer_phonenumber(message: types.Message, state: FSMContext):
    number = message.text
    await state.update_data({"number": number})
    await message.answer("Joylashuvni yuboring:", reply_markup=location_button)
    await PersonalData.next()


# Joylashuvni qabul qilish
@dp.message_handler(content_types=types.ContentType.LOCATION, state=PersonalData.location)
async def answer_location(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    number = data.get("number")
    latitude = message.location.latitude
    longitude = message.location.longitude

    msg = (
        f"Quyidagi ma'lumotlar qabul qilindi:\n"
        f"Ismingiz: {name}\n"
        f"Telefon: {number}\n"
        f"Joylashuv: {latitude}, {longitude}"
    )
    await message.answer(msg, reply_markup=userButton)

    # State dan chiqaramiz
    await state.finish()
    await state.reset_state()

################ sozlamalar uchun
@dp.message_handler(text='sozlamalar')
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting",reply_markup=types.ReplyKeyboardRemove())
    await PersonalData.fullName.set()


# Ismni qabul qilish
@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"name": fullname})
    await message.answer("Telefon raqamingizni kiriting:")
    await PersonalData.next()


# Telefon raqamini qabul qilish
@dp.message_handler(state=PersonalData.phonenumber)
async def answer_phonenumber(message: types.Message, state: FSMContext):
    number = message.text
    await state.update_data({"number": number})
    await message.answer("Joylashuvni yuboring:", reply_markup=location_button)
    await PersonalData.next()


# Joylashuvni qabul qilish
@dp.message_handler(content_types=types.ContentType.LOCATION, state=PersonalData.location)
async def answer_location(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    number = data.get("number")
    latitude = message.location.latitude
    longitude = message.location.longitude

    

    # State dan chiqaramiz
    await state.finish()
    await state.reset_state()
    msg1 = (
        f"shaxsiy ma'lumotlar yangilandi:\n"
        f"Ismingiz: {name}\n"
        f"Telefon: {number}\n"
        f"Joylashuv: {latitude}, {longitude}"
    )
    await message.answer(msg1, reply_markup=userButton)