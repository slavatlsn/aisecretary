import os
from cozepy import COZE_COM_BASE_URL
from cozepy import AsyncCoze, Coze, TokenAuth

coze_api_token = os.getenv("COZE_API_TOKEN")
coze_api_base = COZE_COM_BASE_URL

coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)
async_coze = AsyncCoze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)