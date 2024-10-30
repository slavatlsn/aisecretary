from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageObjectString
from my_token import token as t
from pathlib import Path

coze = Coze(auth=TokenAuth(t))

#file = coze.files.upload(file=Path('/filepath'))
s = ''

file = coze.files.upload(file='file.txt')
print(file)
chat_poll = coze.chat.create_and_poll(bot_id='7422700799514099718', user_id='0', additional_messages=[Message.build_user_question_text("Сократи текст" + s + 'и выдай ответ в формате *.pdf')])
#chat_poll = coze.chat.create_and_poll(bot_id='7422700799514099718', user_id='0', additional_messages=[Message.build_user_question_objects(MessageObjectString.build_file())])


for message in chat_poll.messages:
    print(message.content, end="")

if chat_poll.chat.status == ChatStatus.COMPLETED:
    print()
    print("token usage:", chat_poll.chat.usage.token_count)
