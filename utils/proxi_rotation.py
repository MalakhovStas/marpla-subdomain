import random
import time
from typing import Optional, Dict, Tuple

from utils.utils_config import TIME_QUARANTINE_PROXI, PROXIES, headers

PROXIES_Status = []


def func_proxi_rotation(bad_proxi: Optional[Dict] = None, stop_proxies={}) -> Tuple:
    """
    Модуль для ротации и карантина прокси, если при вызове функции указан bad_proxi он попадает в карантин на срок,
    указанный в переменной TIME_CARANTIN_PROXI в секундах.
    """

    for tm, pr in stop_proxies.copy().items():
        if time.time() - tm >= TIME_QUARANTINE_PROXI:
            stop_proxies.pop(tm)

    if bad_proxi and bad_proxi not in stop_proxies.values():
        # print(f'Прокси {bad_proxi} попал в карантин, всего в карантине {len(stop_proxies)} прокси')
        stop_proxies[time.time()] = bad_proxi

    while True:
        working_proxi = [prx for prx in PROXIES if prx not in stop_proxies.values() and prx not in PROXIES_Status]
        proxi = random.choice(working_proxi)
        if proxi not in stop_proxies.values() and proxi not in PROXIES_Status:
            # print(f'выдал прокси {proxi}')
            PROXIES_Status.append(proxi)
            return headers, proxi

        # print(f'этот {proxi} занят, в карантине: {len(stop_proxies)}')
