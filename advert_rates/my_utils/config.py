""" Параметры HTML запросов к API Wildberries """
WB_CATALOG = 'https://catalog-ads.wildberries.ru/api/v5/search?keyword='
WB_CAROUSEL = 'https://carousel-ads.wildberries.ru/api/v4/carousel?nm='
LinkSTART = 'https://www.wildberries.ru/catalog/'
LinkEND = '/detail.aspx'

""" Количество продуктов к выдаче пользователям """
NUM_PROD = 100

""" Данные для работы с прокси"""
TIME_QUARANTINE_PROXI = 1200
login_password = 'bowiabti:kxte07lwuxk0'
UA_and_PROXIES = {
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36': {
        'https': f'socks5://{login_password}@64.43.90.255:6770'},
    'Mozilla/5.0 (X11; Linux i686; rv:103.0) Gecko/20100101 Firefox/103.0': {
        'https': f'socks5://{login_password}@113.30.153.73:5409'},
    'Mozilla/5.0 (Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0': {
        'https': f'socks5://{login_password}@138.128.107.175:8764'},
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:103.0) Gecko/20100101 Firefox/103.0': {
        'https': f'socks5://{login_password}@91.246.194.229:6742'},
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0': {
        'https': f'socks5://{login_password}@186.179.23.24:5068'},
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0': {
        'https': f'socks5://{login_password}@80.253.249.169:5212'},
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 OPR/89.0.4447.71': {
        'https': f'socks5://{login_password}@45.86.63.188:6256'},
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 Vivaldi/5.3.2679.70': {
        'https': f'socks5://{login_password}@45.128.76.175:6176'},
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 Vivaldi/5.3.2679.70': {
        'https': f'socks5://{login_password}@194.31.162.32:7548'},
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 YaBrowser/22.7.0 Yowser/2.5 Safari/537.36': {
        'https': f'socks5://{login_password}@182.54.239.39:8056'},
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 YaBrowser/22.7.0 Yowser/2.5 Safari/537.36': {
        'https': f'socks5://{login_password}@192.186.185.121:6680'},
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 Vivaldi/5.3.2679.70': {
        'https': f'socks5://{login_password}@104.227.1.145:7741'},
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 Vivaldi/5.3.2679.70': {
        'https': f'socks5://{login_password}@80.253.250.113:5450'},
    'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 OPR/89.0.4447.71': {
        'https': f'socks5://{login_password}@45.130.60.21:9548'},
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 OPR/89.0.4447.71': {
        'https': f'socks5://{login_password}@45.192.157.164:6291'},
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/104.0.0.0 Safari/537.36 Edg/104.0.1293.47': {
        'https': f'socks5://{login_password}@45.8.134.157:7173'},
    'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko': {
        'https': f'socks5://{login_password}@138.128.40.149:6152'},
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0': {
        'https': f'socks5://{login_password}@23.229.125.226:9255'}}

# pip install -U requests[socks]
# 'https://httpbin.org/ip' - возвращает ip адрес в json формате