from aiogram import Bot,Dispatcher,types,executor
import config
import sqlite3


bot = Bot(token = config.token)
dp = Dispatcher(bot)

connect = sqlite3.connect('users.dp')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id_user INTEGER,
    chat_id INTEGER
    );
    """)
connect.commit()


@dp.message_handler(commands= 'start')
async def start(message:types.Message):
    await message.answer(f"As salamu aleykum {message.from_user.full_name} \n" 
                        f'Добро пожаловать в Geektech!')

    cursor = connect.cursor()
    cursor.execute(f"SELECT id_user FROM users WHERE id_user = {message.from_user.id};")
    res = cursor.fetchall()
    if res == []:
        cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}',
        '{message.from_user.first_name}','{message.from_user.last_name}',
        {message.from_user.id}, {message.chat.id})""")
    connect.commit()
    await message.answer(f"Здраствуйте {message.from_user.full_name}")


@dp.message_handler(commands= 'beckend')
async def beckend(messsage:types.Message):
    await messsage.answer(f'''Beckend — это разработка бизнес-логики продукта
                        сайта или веб-приложения. 
                        Beckend отвечает за взаимодействие пользователя с внутренними данными,
                        которые потом отображает фронтенд.''')
    await messsage.answer(f"Стоимость курса 10000 сом в месяц")
    await messsage.answer(f"Обучуение: 5 месяц")     

@dp.message_handler(commands= 'frontend')
async def beckend(messsage:types.Message):
    await messsage.answer(f'''Frontend — это разработка пользовательского интерфейса и функций,
     которые работают на клиентской стороне веб-сайта или приложения''')
    await messsage.answer(f"Стоимость курса 10000 сом в месяц")
    await messsage.answer(f"Обучуение: 5 месяц")  

@dp.message_handler(commands= ' uxui')
async def beckend(messsage:types.Message):
    await messsage.answer(f''' UX/UI-дизайнеры востребованы в IT-сфере,
     поскольку интерфейсы, которые готовят программисты,
      должны быть не только красивы, но и понятны''')
    await messsage.answer(f"Стоимость курса 10000 сом в месяц")
    await messsage.answer(f"Обучуение: 5 месяц")  

@dp.message_handler(commands= 'ios')
async def beckend(messsage:types.Message):
    await messsage.answer(f'''— мобильная операционная система для смартфонов''')
    await messsage.answer(f"Стоимость курса 10000 сом в месяц")
    await messsage.answer(f"Обучуение: 5 месяц")  

@dp.message_handler(commands= 'android')
async def beckend(messsage:types.Message):
    await messsage.answer(f'''Android-это мобильная операционная система,
    основанная на модифицированной версии ядра Linux и другого 
    программного обеспечения с открытым исходным кодом''')
    await messsage.answer(f"Стоимость курса 10000 сом в месяц")
    await messsage.answer(f"Обучуение: 5 месяц")  



executor.start_polling(dp)

