import re

from . import request_api
from . import response_request
from .config import WB_CAROUSEL, WB_CATALOG


def func_search(message: str) -> str:
    """ Обработчик сообщения полученного в состоянии реклама в карточке, выделяет из сообщения номер карточки товара для
        запроса на API WB """

    if message.strip().isdigit() or message.strip().startswith('https:'):

        result = re.search(r'[^\/]{0,1}(\d+)[^\/]{0,1}', message)
        nmid = str(result.group(0)) if result else ''

        if not nmid:
            text = '&#129302 Возможно указанная ссылка не соответствует ожидаемой, ' \
                   'пример: https://www.wildberries.ru/catalog/39337945/detail.aspx\n' \
                   'также можно указать артикул товара, пример: <b>39337945</b>\n' \
                   'Попробуйте ещё раз или сбросьте запрос &#128073 /reset'
        else:
            response = request_api.func_request(url=WB_CAROUSEL + nmid)
            text = response_request.func_response(message=message, response=response, call='card_request',
                                                  nmid=nmid, url=WB_CAROUSEL + nmid)
    else:
        url = WB_CATALOG + '%20'.join(message.strip().split())
        response = request_api.func_request(url=url)
        text = response_request.func_response(message=message, response=response, call='search_request', url=url)
        # text = '&#129302 При запросе <b>"Реклама в карточке"</b> необходимо ввести ссылку на товар, пример: ' \
        #        'https://www.wildberries.ru/catalog/39337945/detail.aspx\n ' \
        #        'или его артикул, пример: <b>39337945</b>\nПопробуйте ещё раз или сбросьте запрос &#128073 /reset'

    return text


# https://www.wildberries.ru/catalog/25356409/detail.aspx

# print(func_search('https://www.wildberries.ru/catalog/39337945/detail.aspx'))
# print(func_search('штаны'))
