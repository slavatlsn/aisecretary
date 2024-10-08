import requests

class Coze():
    token = ''

    def __init__(self, access_token):
        self.token = access_token

    def create_conversation(self):
        headers = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        resp = requests.post('https://api.coze.com/v1/conversation/create', headers=headers).json()
        return resp

    def send_text_message(self, conv_id, text):
        headers = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        query = {'conversation_id': conv_id} # conv_id - string
        message = {
            "role": "user",
            "content": text,
            "content_type": "text"
        }
        resp = requests.post(' https://api.coze.com/v1/conversation/message/create', headers=headers, params=query, json=message).json()
        return resp
