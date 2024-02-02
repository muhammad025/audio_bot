import logging

from aiogram import Bot, Dispatcher, executor, types
from butoon import bosh_menu,ikkinchi_menu,iki_menu

API_TOKEN = '5646352744:AAFvV_9K-mooNo9B11K4-a69CRLGNrXDeCU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup=bosh_menu)

@dp.message_handler(text="💿 Jahon adabiyoti 💿")
async def echo(message: types.Message):
    await message.answer("🔘 Tanlang",reply_markup=ikkinchi_menu)

@dp.message_handler(text="Choliqushi")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1873''')

@dp.message_handler(text="Qon da'vosi")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1664 ''')

@dp.message_handler(text="Martin Iden")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2156 ''')

@dp.message_handler(text="Hikoyalar (Jek London)")
async def echo(message: types.Message):
    await message.answer(''' Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/587''')

@dp.message_handler(text="Taras Bulba")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/2179 ''')


@dp.message_handler(text="Usta va Margarita")
async def echo(message: types.Message):
    await message.answer(''' Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1935''')


@dp.message_handler(text="💿 O‘zbek adabiyoti 💿")
async def echo(message: types.Message):
    await message.answer(text="🔘 Tanlang",reply_markup=iki_menu)

@dp.message_handler(text="O'tkan kunlar")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/933''')

@dp.message_handler(text="Ufq")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/406''')

@dp.message_handler(text="Avlodlar dovoni")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/1014 ''')

@dp.message_handler(text="Mehrobdan chayon")
async def echo(message: types.Message):
    await message.answer(''' Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/700''')

@dp.message_handler(text="Kecha va kunduz")
async def echo(message: types.Message):
    await message.answer('''Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/275''')


@dp.message_handler(text="Yulduzli tunlar")
async def echo(message: types.Message):
    await message.answer(''' Bu yerdan yuklab oling:

https://t.me/audiokitoblar_uz/890''')


@dp.message_handler(text="⬅Ortga")
async def echo(message: types.Message):
    await message.answer(".",reply_markup=bosh_menu)

    

@dp.message_handler(text="🔘 Audio darsliklar 🔘")
async def echo(message: types.Message):
    await message.answer("Audio darsliklar bu yerda: @audio_darsliklar")


@dp.message_handler(text="🔘 Yangi audio kitoblar 🔘")
async def echo(message: types.Message):
    await message.answer("""
Yangi audio kitoblarni o‘tkazib yubormaslik uchun kanalimizga obuna bo‘lishni unutmang: 

t.me/audiokitoblar_uz""")


@dp.message_handler(text="📨 Murojaat uchun 📨")
async def echo(message: types.Message):
    await message.answer("""Murojaat uchun: 

@audiokitoblar_uzbot""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)