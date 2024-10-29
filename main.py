import telebot
from telebot import types

bot = telebot.TeleBot('7973744367:AAExS_wxcfVy74mFYRInAWXa8CWch0G0yJU')
states = dict()

@bot.message_handler(content_types=['text', 'document', 'audio', 'voice'])
def starting_messages(message):
    print(states)
    print(message)
    if message.from_user.id in states.keys() and states[message.from_user.id] == 1:
        if message.content_type == 'document':
            f_id = message.document.file_id
        elif message.content_type == 'audio':
            f_id = message.audio.file_id
        elif message.content_type == 'voice':
            f_id = message.voice.file_id
        elif message.content_type == 'text':
            txt = message.text
        # загружаем документ и проверяем формат pdf, docx, wav, mp3
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Привет!\nЯ помогаю сократить содержимое файлов и текстовых сообщений")
        states[message.from_user.id] = 1
        #добавить кнопочку внизу "закончить загрузку данных"
        #input_data_type(message)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start")




def input_data_type(message):


    '''
    keyboard = types.InlineKeyboardMarkup()
    button_doc = types.InlineKeyboardButton(text='docx', callback_data='doc/docx')
    button_pdf = types.InlineKeyboardButton(text='pdf', callback_data='pdf')
    button_txt = types.InlineKeyboardButton(text='Текстовое сообщение', callback_data='txt')
    #button_mp3 = types.InlineKeyboardButton(text='mp3', callback_data='mp3')
    #button_wav = types.InlineKeyboardButton(text='wav', callback_data='wav')
    #button_audio = types.InlineKeyboardButton(text='Голосовое сообщение', callback_data='audio')
    buttons = [button_doc, button_pdf, button_txt, button_mp3, button_wav, button_audio]
    keyboard.add(*buttons)
    bot.send_message(message.from_user.id, "Выберите тип входных данных", reply_markup=keyboard)
    '''

def uploading_files(message):
    bot.send_message(message.from_user.id, "Загрузите файлы в порядке обработки данных")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    uploading_files(call.data)


bot.polling(none_stop=True, interval=0)





