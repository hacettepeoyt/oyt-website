import json

import requests
from django.conf import settings


def send_message_to_admin_room(message):
    MATRIX_ADMIN_ROOM = settings.CONFIG['MATRIX_ADMIN_ROOM']
    MATRIX_ACCESS_TOKEN = settings.CONFIG['MATRIX_ACCESS_TOKEN']

    url = (f'https://matrix.org/_matrix/client/r0/rooms/{MATRIX_ADMIN_ROOM}/send'
           f'/m.room.message?access_token={MATRIX_ACCESS_TOKEN}')
    headers = {'Content-Type': 'application/json'}
    data = {
        'msgtype': 'm.text',
        'body': message
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()
    else:
        error = f'Matrix returned status code: {response.status_code}'
        error_response = response.json()
        raise Exception(error, error_response)
