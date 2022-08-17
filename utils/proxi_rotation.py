import random
import time
from typing import Optional, Dict, Tuple

from utils.utils_config import TIME_QUARANTINE_PROXI, UA_and_PROXIES


def func_proxi_rotation(bad_proxi: Optional[Dict] = None, stop_proxies={}) -> Tuple:
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
