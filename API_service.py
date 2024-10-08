import requests

class Coze():
    token = ''

    def __init__(self, access_token):
        self.token = access_token

    def create_conversation(self):
        headers = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        print(requests.post('https://api.coze.com/v1/conversation/create', headers=headers))
