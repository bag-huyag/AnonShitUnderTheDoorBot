import telebot
from telebot import types  # для указание типов

token = ''

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("👋 Поздороваться")
    btn1 = types.KeyboardButton("Сделать заказ")

    # btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn2 = types.KeyboardButton("Хочу стать сотрудником")

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот для тех, кто очень хочет насрать под дверь своему другу, но не может. Наши сотрудники помогут тебе.".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Хочу стать сотрудником"):
        # bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
        bot.send_message(message.chat.id, text="В данный момент открыта вакансия для доставщиков и исполнителей заказов! отправь мне своё резюме и мы с тобой обязательно свяжемся")

    elif (message.text == "Сделать заказ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton("Как меня зовут?")
        btn1 = types.KeyboardButton("Упаковать в подарочную коробку")
        # btn2 = types.KeyboardButton("Что я могу?")
        btn2 = types.KeyboardButton("Добавить записку для получателя")
        btn3 = types.KeyboardButton("Дополнительные пожелания")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Сделай заказ", reply_markup=markup)



    elif (message.text == "Упаковать в подарочную коробку"):
        bot.send_message(message.chat.id, "Будет сделано! Пришли мне адрес получателя для продолжения")
    # elif (message.text != "Упаковать в подарочную коробку" and message.text != "Сделать заказ"):
    #         bot.send_message(message.chat.id, "Супер! наши администраторы обработают твою заявку и вышлют ответ.")

    elif (message.text == "Добавить записку для получателя"):
        bot.send_message(message.chat.id, text="Добавить записку для получателя и написать адрес доставки:")
    # elif (message.text != "Добавить записку для получателя" and message.text != "Сделать заказ"):
    #         bot.send_message(message.chat.id, "Будет сделано! Пришли мне адрес получателя для продолжения")

    elif message.text == "Дополнительные пожелания":
        bot.send_message(message.chat.id, text="Напишите о дополнительных пожеланиях и адрес доставки.")
    # elif (message.text != "Дополнительные пожелания" and message.text != "Сделать заказ"):
    #         bot.send_message(message.chat.id, "Пришли мне адрес получателя для продолжения")

    elif (message.text == "Вернуться в главное меню"):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # button1 = types.KeyboardButton("👋 Поздороваться")
        button1 = types.KeyboardButton("Хочу стать сотрудником")
        # button2 = types.KeyboardButton("❓ Задать вопрос")
        button2 = types.KeyboardButton("Сделать заказ")

        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    else:
            # bot.send_message(message.chat.id, "Мы ответим тебе в ближайщее время.")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Хочу стать сотрудником")
            button2 = types.KeyboardButton("Сделать заказ")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="Заказ принят. Мы ответим тебе в ближайщее время.", reply_markup=markup)



bot.polling(none_stop=True)