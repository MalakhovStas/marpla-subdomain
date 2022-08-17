import sqlite3

import requests

from utils.proxi_rotation import func_proxi_rotation
from utils.utils_config import path_db, url_subject, WBToken, x_supplier_id


class Database:
    """Класс описывающий работу приложения с базой данных"""

    def __init__(self, path_db):
        self.database = sqlite3.connect(path_db)
        self.cursor = self.database.cursor()

    def select_subject_id(self, objectId):
        with self.database:
            self.cursor.execute("SELECT objectName FROM wb_subjects WHERE objectId = ?", (objectId,))
            i_data = self.cursor.fetchone()
            i_data = i_data[0] if i_data else i_data
            return i_data

    def select_subject_name(self, objectName):
        with self.database:
            self.cursor.execute("SELECT objectName FROM wb_subjects WHERE objectName = ?", (objectName,))
            i_data = self.cursor.fetchone()
            i_data = i_data[0] if i_data else i_data
            return i_data

    def insert_subject(self, objectId, objectName, parentId, parentName, isVisible) -> None:
        with self.database:
            self.cursor.execute("INSERT INTO wb_subjects(objectId, objectName, parentId, parentName, isVisible) VALUES "
                                "(?, ?, ?, ?, ?)", (objectId, objectName, parentId, parentName, isVisible))
            self.database.commit()


def func_request(subject_name):
    for _ in range(3):
        try:
            user_agent, proxi = func_proxi_rotation()
            resp = requests.get(url=url_subject, headers={'User-Agent': user_agent}, proxies=proxi,
                                cookies={'WBToken': WBToken, 'x-supplier-id': x_supplier_id},
                                params={'name': subject_name}).json().get('data')
            if resp:
                return resp
        except Exception as exc:
            print(f'\033[31mОшибка запроса - повторяю запрос\033[0m Ошибка: {exc}')
    else:
        print(f'\033[31mНе удалось получить данные по предмету - \033[0m{subject_name}')
        return []


db = Database(path_db=path_db)

with open('subjects_names.csv', 'r') as file:
    data = file.read().strip().split('\n')

sum_add_subjects = 0
for num, name in enumerate(data[:100]):
    if db.select_subject_name(objectName=name):
        print(f'{num + 1}. \033[35m{name} - \033[31mесть в базе данных , перехожу к следующему\033[0m')
        continue
    else:
        response = func_request(subject_name=name)
        if not response:
            print('ошибка в response нет значений')
        else:
            for num_in_num, subject in enumerate(response):
                objectId = subject.get('objectId')
                objectName = subject.get('objectName')
                parentId = subject.get('parentId')
                parentName = subject.get('parentName')
                isVisible = str(subject.get('isVisible'))

                subj_in_base = db.select_subject_id(objectId=objectId)
                if subj_in_base == objectName:
                    print(f'{num + 1}-{num_in_num + 1}. \033[35m{subj_in_base} - '
                          f'\033[31mесть в базе данных , перехожу к следующему\033[0m')
                    continue
                else:
                    db.insert_subject(objectId, objectName, parentId, parentName, isVisible)
                    print(f'{num + 1}-{num_in_num + 1}. \033[35m{objectName} - \033[32mдобавлен в базу данных\033[0m')
                    sum_add_subjects += 1

print(f'\033[33mВ базу добавлено \033[0m{sum_add_subjects} \033[33mпредметов\033[0m')
