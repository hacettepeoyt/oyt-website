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


def get_client_ip(request) -> tuple[str, str]:
    """
    Returns the client's IP address and its source from the request.

    Tries to obtain the IP from the 'HTTP_X_FORWARDED_FOR' header
    if available, otherwise uses 'REMOTE_ADDR'.

    Args:
        request: An HTTP request object.

    Returns:
        A tuple containing:
            - The client's IP address as a string.
            - The source of the IP address ('HTTP_X_FORWARDED_FOR' or 'REMOTE_ADDR').
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        source = 'HTTP_X_FORWARDED_FOR'
    else:
        ip = request.META.get('REMOTE_ADDR')
        source = 'REMOTE_ADDR'

    return ip, source
