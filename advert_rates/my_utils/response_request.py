from typing import Dict, List
from . import config


def func_response(message: str, response: Dict | List, call: str, nmid: str = None, url: str = None) -> str | list | None:
    """Формирует и отравляет ответ на запрос пользователя"""

    if isinstance(response, Dict):
        adverts = response.get('adverts')
        key_id = 'id'
    else:
        adverts = response
        key_id = 'nmId'

    # req_type = 'реклама в карточке' if current_state.endswith('card_request') else 'реклама в поиске'
    # answer = '' if (adverts and adverts != 'null') else '\n<b>Ответ:</b> Некорректный запрос'
    # await admins_send_message.func_admins_message(update=message,
    #                                               message=f'<b>ID:</b> {message.from_user.id}, '
    #                                                       f'<b>Имя:</b> {message.from_user.first_name}\n'
    #                                                       f'<b>Контакт:</b> <a href="tg://user?id='
    #                                                       f'{message.from_user.id}">{message.from_user.username}</a>\n'
    #                                                       f'<b>Тип:</b> {req_type}\n'
    #                                                       f'<b>Запрос:</b> {message.text}{answer}')

    # if adverts and adverts != 'null':
    #     line = 'Реальные ставки рекламы в\n'
    #     if call == 'card_request':
    #         line += f"карточке товара по артикулу: " \
    #                f"<b><i><a href='{config.LinkSTART}{nmid}{config.LinkEND}'>{nmid}</a></i></b>\n\n"
    #
    #     elif call == 'search_request':
    #         line += f"поиске по запросу: <b><i>{message}</i></b>\n\n"
    #
    #     for num, advert in enumerate(adverts):
    #         product_id = advert.get(key_id)
    #         cpm = str("{:,.0f}".format(advert.get('cpm')).replace(",", " "))
    #         # emodji = f'&#{49 + num};&#65039;&#8419;' if num < 9 else '&#128287'
    #         line += f"{num+1} " \
    #                 f"Позиция <b><a href='{config.LinkSTART}" \
    #                 f"{product_id}{config.LinkEND}'>{product_id}</a></b> " \
    #                 f"Ставка <b>{cpm} руб.</b>"
    #         if num == config.NUM_PROD:
    #             break
    #
    # else:
    #     line = 'К сожалению по вашему запросу ничего не найдено, возможно фраза написана с ошибками. ' \
    #            'Попробуйте отправить другой запрос или обратитесь в поддержку'
    if adverts and adverts != 'null':
        answer = list()
        for number, advert in enumerate(adverts):
            product_id = advert.get(key_id)
            cpm = str("{:,.0f}".format(advert.get('cpm')).replace(",", " "))
            answer.append({'number': number+1, 'product_id': product_id, 'cpm': cpm})
    else:
        return None

    # return line
    return answer
