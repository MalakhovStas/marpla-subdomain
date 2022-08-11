import json
from typing import List, Dict

import requests

from . import proxi_rotation


def func_request(url: str) -> Dict | List:
    """ Запрашивает данные с API сайта(url), в случае успеха возвращает полученное сообщение в виде словаря или списка,
        в противном случае возвращает пустой словарь и отправляет сообщение об ошибке запроса администраторам """

    user_agent, proxi = proxi_rotation.func_rotation()

    for step in range(1, 4):
        if step > 1:
            user_agent, proxi = proxi_rotation.func_rotation(bad_proxi=proxi)

        response_api = requests.get(url=url, headers={'User-Agent': user_agent}, proxies=proxi)

        if response_api.status_code == requests.codes.ok and response_api.text:
            return json.loads(response_api.text)

    return dict()
