import json
import re
from typing import Dict, List, Union

import requests

from advert_rates.models import WBSubject
from utils.proxi_rotation import func_proxi_rotation
from utils.utils_config import LinkSTART, LinkEND, WB_CAROUSEL, WB_CATALOG


def func_request(url: str) -> Dict:
    """ Запрашивает данные с API сайта(url), в случае успеха возвращает полученное сообщение в виде словаря или списка,
        в противном случае возвращает пустой словарь и отправляет сообщение об ошибке запроса администраторам """

    user_agent, proxi = func_proxi_rotation()

    for step in range(1, 4):
        if step > 1:
            user_agent, proxi = func_proxi_rotation(bad_proxi=proxi)

        response_api = requests.get(url=url, headers={'User-Agent': user_agent}, proxies=proxi)

        if response_api.status_code == requests.codes.ok and response_api.text:
            # print(response_api.text)
            return json.loads(response_api.text)

    return {}


def func_search_img(product_id):
    if len(str(product_id)) == 7:
        vol = 2
        part = 4
    elif len(str(product_id)) == 8:
        vol = 3
        part = 5
    elif len(str(product_id)) == 9:
        vol = 4
        part = 6

    if int(str(product_id)[0]) == 1:
        if len(str(product_id)) == 7:
            domen = 'basket-01'

        elif len(str(product_id)) == 8:
            if product_id > 14399999:
                domen = 'basket-02'
            else:
                domen = 'basket-01'

        elif len(str(product_id)) == 9:
            if product_id > 111599999:
                if product_id > 116999999:
                    domen = 'basket-09'
                else:
                    domen = 'basket-08'
            else:
                domen = 'basket-07'

    elif int(str(product_id)[0]) == 2:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        elif len(str(product_id)) == 8:
            if product_id > 28799999:
                domen = 'basket-03'
            else:
                domen = 'basket-02'
        else:
            domen = 'basket-02'

    elif int(str(product_id)[0]) == 3:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        else:
            domen = 'basket-03'

    elif int(str(product_id)[0]) == 4:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        elif len(str(product_id)) == 8:
            if product_id > 43199999:
                domen = 'basket-04'
            else:
                domen = 'basket-03'

    elif int(str(product_id)[0]) == 5:
        domen = 'basket-04'

    elif int(str(product_id)[0]) == 6:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        else:
            domen = 'basket-04'

    elif int(str(product_id)[0]) == 7:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        else:
            if product_id > 71999999:
                domen = 'basket-05'
            else:
                domen = 'basket-04'

    elif int(str(product_id)[0]) == 8:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        elif len(str(product_id)) == 8:
            domen = 'basket-05'
    elif int(str(product_id)[0]) == 9:
        if len(str(product_id)) == 7:
            domen = 'basket-01'
        else:
            domen = 'basket-05'

    else:
        domen = 'basket-01'
    link_img = f'https://{domen}.wb.ru/vol{str(product_id)[:vol]}/part{str(product_id)[:part]}/{product_id}/' \
               f'images/c246x328/1.jpg'
    return link_img


def func_response(response: Dict) -> Union[Dict, List]:
    """ Формирует и отравляет ответ на запрос пользователя """
    answer = []

    if isinstance(response, Dict):
        adverts = response.get('adverts')
        # prioritySubjects = response.get('prioritySubjects')
        key_id = 'id'
        subject_key = 'subject'
    else:
        adverts = response
        key_id = 'nmId'
        subject_key = 'subjectId'

    if adverts and adverts != 'null':
        for number, advert in enumerate(adverts):
            product_id = advert.get(key_id)
            cpm = str("{:,.0f}".format(advert.get('cpm')).replace(",", " "))
            link = f'{LinkSTART}{product_id}{LinkEND}'
            subject_id = advert.get(subject_key)
            mdd = WBSubject.objects.filter(objectId__iexact=subject_id)
            subject_name = mdd[0].objectName if mdd else None
            img = func_search_img(product_id=product_id)
            answer.append({"position": number + 1, "product_id": product_id, "cpm": cpm, "link": link, "img": img,
                           "subject": {"id": subject_id, "name": subject_name}})
    return answer


def func_search(message: str) -> Dict:
    """
     Обработчик сообщения полученного в состоянии реклама в карточке, выделяет из сообщения номер карточки товара для
     запроса на API WB
    """
    message = message.strip().lower()
    if 'ё' in message:
        message = message.replace('ё', 'е')
    if message.strip().isdigit() or message.strip().startswith('https:'):
        query_type = 'article' if message.strip().isdigit() else 'url'

        pattern = re.search(r'[^\/]{0,1}(\d+)[^\/]{0,1}', message)
        nmid = str(pattern.group(0)) if pattern else ''

        if nmid:
            response = func_request(url=WB_CAROUSEL + nmid)
            result = func_response(response=response)

        else:
            result = []
    else:
        query_type = 'keyword'
        url = WB_CATALOG + '%20'.join(message.strip().split())
        response = func_request(url=url)
        result = func_response(response=response)

    return {'queryType': query_type, 'response': result}


# https://www.wildberries.ru/catalog/25356409/detail.aspx
# print(func_search('https://www.wildberries.ru/catalog/39337945/detail.aspx'))
# res = func_search('https://www.wildberries.ru/catalog/39337945/detail.aspx')
# print(type(res))
# print(res)
