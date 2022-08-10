import requests
import time

TOKEN = ""

ROOT_URL = f"https://api.telegram.org/bot{TOKEN}"

def set_interval(ms,callback):
    timing = time.time()
    while True:
        if time.time() - timing > ms:
            timing = time.time()
            callback()

def get_update(url,update_id):
    responce = requests.get(f'{url}/getUpdates?offset={update_id + 1}')
    if responce.status_code == requests.codes.ok:       
        return responce.json()
    else:
        get_update(url,update_id)

def send_message(chat_id, message_text,url):
    data = {'chat_id':chat_id ,'text': message_text}
    responce = requests.post(f'{url}/sendMessage',data = data)

answered_update_id = 0	

def compare():
    global answered_update_id
    updates = get_update(ROOT_URL,answered_update_id)
    if updates.get('result'):
        update_id = updates.get('result')[0]['update_id']
        if update_id != answered_update_id:
            chat_id = updates.get('result')[0]['message']['chat']['id']
            message_text = updates.get('result')[0]['message']['text']
            send_message(chat_id,message_text,ROOT_URL)
            answered_update_id = update_id

set_interval(4.0,compare)
