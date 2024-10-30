import telebot
from telebot import types
from token import token as t
from cozepy import Coze, TokenAuth, Message, ChatStatus
import os

#file = coze.files.upload(file=Path('/filepath'))

coze = Coze(auth=TokenAuth(t))


for message in chat_poll.messages:
    print(message.content, end="")

bot = telebot.TeleBot(t)
states = dict()

@bot.message_handler(content_types=['text', 'document', 'audio', 'voice'])
def starting_messages(message):

    print(message)
    # добавление нового пользователя на момент данной сессии
    if message.from_user.id not in states.keys():
        states[message.from_user.id] = [0, "", ""]

    # стартовое сообщение
    if states[message.from_user.id][0] == 0 or message.text == "/start":
        if message.text == "/start":
            bot.send_message(message.from_user.id, "Привет!\nЯ помогаю сократить содержимое файлов и текстовых сообщений")
            states[message.from_user.id][0] = 1
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start")

    # добавление файла (подумать как сказать пользователю, что у него не того формата файл)
    if states[message.from_user.id][0] == 1:
        txt = ''
        f_id = ''
        if message.content_type == 'document':
            f_id = message.document.file_id
        elif message.content_type == 'audio':
            f_id = message.audio.file_id
        elif message.content_type == 'voice':
            f_id = message.voice.file_id
        elif message.content_type == 'text' and message.text != "/start":
            txt = message.text

        if txt != '' or f_id != '':
            if f_id != '':
                states[message.from_user.id][2] = "f_id" + f_id
            else:
                states[message.from_user.id][2] = txt
            print(txt, f_id)
            states[message.from_user.id][0] = 2
        else:
            bot.send_message(message.from_user.id, "Добавь входные данные в виде текстового или голосового сообщения, или в формате docx, pdf, wav, mp3")

    if states[message.from_user.id][0] == 2:
        button_doc = types.KeyboardButton(text='docx')
        button_pdf = types.KeyboardButton(text='pdf')
        button_txt = types.KeyboardButton(text='Текстовое сообщение')
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        button = [button_txt, button_doc, button_pdf]
        keyboard.add(*button)
        if message.text in ['docx', 'pdf', 'Текстовое сообщение']:
            states[message.from_user.id][0] = 3
        else:
            bot.send_message(message.from_user.id, "В каком формате вывести выходные данные?", reply_markup=keyboard)

    # отправка и получение данных от козы
    if states[message.from_user.id][0] == 3:
        telebot.types.ReplyKeyboardRemove()
        states[message.from_user.id][1] = message.text
        print(states[message.from_user.id][0], states[message.from_user.id][1], message.from_user.id)
        #получение данных от нейросети
        #ожидание ответа
        #если ответ пришел отправка ответа в нужном формате и

        # по нормальному прописать переход к началу цикла, после выгрузки с козы
        states[message.from_user.id][0] = 1
'''
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    states[call.from_user.id][1] = call.data
    print(states)
'''

bot.polling(none_stop=True, interval=0)





