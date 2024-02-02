from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=
    [
     
        [
            KeyboardButton(text="💿 O‘zbek adabiyoti 💿"),
            KeyboardButton(text="💿 Jahon adabiyoti 💿"),
        
        ],
        [
            KeyboardButton(text="🔘 Audio darsliklar 🔘"),
        ],

        [
            KeyboardButton(text="🔘 Yangi audio kitoblar 🔘"),
        ],
         [
            KeyboardButton(text="📨 Murojaat uchun 📨"),
        ],
        [
            KeyboardButton(text="⬅Ortga")
        ]
],
resize_keyboard=True
)

iki_menu = ReplyKeyboardMarkup(
    keyboard=
    [
     
        [
            KeyboardButton(text="O'tkan kunlar"),
            KeyboardButton(text="Ufq"),
        
        ],
        [
            KeyboardButton(text="Avlodlar dovoni"),
               KeyboardButton(text="Mehrobdan chayon"),
        ],

         [
            KeyboardButton(text="Kecha va kunduz"),
             KeyboardButton(text="Yulduzli tunlar")
        ],
        [
            KeyboardButton(text="⬅Ortga")
        ]
],
resize_keyboard=True
)


ikkinchi_menu = ReplyKeyboardMarkup(
    keyboard=
    [
     
        [
            KeyboardButton(text="Choliqushi"),
            KeyboardButton(text="Qon da'vosi"),
        
        ],
        [
            KeyboardButton(text="Martin Iden"),
            KeyboardButton(text="Hikoyalar (Jek London)"),
        ],

        [
            KeyboardButton(text="Taras Bulba"),
            KeyboardButton(text="Usta va Margarita"),
        ],
        
        [
            KeyboardButton(text="⬅Ortga")
        ]
],
resize_keyboard=True
)