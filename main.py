import telebot

bot = telebot.TeleBot('7973744367:AAExS_wxcfVy74mFYRInAWXa8CWch0G0yJU')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Выберете тип загрузки данных")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        .... #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
         ... #переспрашиваем

bot.polling(none_stop=True, interval=0)
