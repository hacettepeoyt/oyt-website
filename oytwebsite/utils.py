import json
import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_message_to_admin_room(message):
    MATRIX_ADMIN_ROOM = settings.CONFIG.get('MATRIX_ADMIN_ROOM')
    MATRIX_ACCESS_TOKEN = settings.CONFIG.get('MATRIX_ACCESS_TOKEN')

    if not MATRIX_ADMIN_ROOM or not MATRIX_ACCESS_TOKEN:
        logger.warning('Matrix configurations are not fully set. '
                       'Sending message to logger instead of matrix admin room.')
        logger.info(message)
        return

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
