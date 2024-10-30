from cozepy import Coze, TokenAuth, Message, ChatStatus
import os
from pathlib import Path

coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")))
chat_poll = coze.chat.create_and_poll(bot_id='bot_id', user_id='user_id', additional_messages=[Message.build_user_question_text("How are you?")])
for message in chat_poll.messages:
    print(message.content, end="")

file = coze.files.upload(file=Path('/filepath'))

coze = Coze(auth=TokenAuth(token))

chat_poll = coze.chat.create_and_poll(bot_id='bot_id', user_id='user_id', additional_messages=[Message.build_user_question_text("Sample message")])

for message in chat_poll.messages:
    print(message.content, end="")