import random
import time
from typing import Dict

from .config import UA_and_PROXIES, TIME_QUARANTINE_PROXI


def func_rotation(bad_proxi: Dict | None = None, stop_proxies={}) -> tuple:
    """
    Модуль для ротации и карантина прокси, если при вызове функции указан bad_proxi он попадает в карантин на срок,
    указанный в переменной TIME_CARANTIN_PROXI в секундах.
    """

    for tm, pr in stop_proxies.items():
        if time.time() - tm >= TIME_QUARANTINE_PROXI:
            stop_proxies.pop(tm)

    if bad_proxi:
        stop_proxies[time.time()] = bad_proxi

    while True:
        user_agent = random.choice(list(UA_and_PROXIES.keys()))
        proxi = UA_and_PROXIES[user_agent]
        if proxi not in stop_proxies.values():
            return user_agent, proxi
