from datetime import datetime, timedelta

from django.db import models


class TelegramUsers(models.Model):
    user_id = models.IntegerField(db_index=True, verbose_name='ТГ user_id', null=False, primary_key=True)
    name = models.CharField(max_length=1000,  default='', db_index=True, verbose_name='имя')
    username = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='ТГ username')
    referer_id = models.PositiveIntegerField(null=True, blank=True, db_index=True, verbose_name='ТГ user_id реферала')
    balance_requests = models.PositiveSmallIntegerField(db_index=True, default=10, null=False, verbose_name='баланс запросов')
    access = models.CharField(max_length=50,  default='allowed', null=False, verbose_name='доступ к боту')
    start_time_limited = models.PositiveIntegerField(null=True, blank=True, verbose_name='время ограничения доступа')
    position = models.CharField(max_length=50, default='user', null=False, verbose_name='роль пользователя')
    password = models.CharField(blank=True, max_length=100, verbose_name='пароль')

    # дальше новые поля
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='когда добавился')
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')

    def __str__(self):
        return f'id: {self.user_id} | Имя: {self.name}'

    class Meta:
        db_table = 'telegram_users'
        ordering = ['date_joined']


class TelegramUsersRequests(models.Model):
    telegram_user = models.ForeignKey('TelegramUsers', on_delete=models.CASCADE, related_name='user',
                                      verbose_name='пользователь', null=False, blank=False, default=1)
    date_request = models.DateTimeField(auto_now_add=True, db_index=True)
    type_request = models.ForeignKey('TypesRequest', on_delete=models.CASCADE, related_name='type_request',
                                     verbose_name='тип запроса')
    text_request = models.CharField(max_length=1000, verbose_name='текст запроса')
    response_status = models.ForeignKey('ResponseStatus', on_delete=models.CASCADE, related_name='response_status',
                                        verbose_name='статус ответа')

    def __str__(self):
        i_view = f'{datetime.date(self.date_request)} | {self.response_status} | {self.telegram_user}'
        return i_view

    class Meta:
        db_table = 'telegram_users_requests'


class TypesRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', default='keyword', primary_key=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_request'


class ResponseStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', default='OK', primary_key=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'response_status'
