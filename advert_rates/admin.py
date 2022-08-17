from django.contrib import admin
from advert_rates.models import TelegramUser, TelegramUserRequest, TypesRequest, ResponseStatus, WBSubject


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TelegramUserRequest)
class TelegramUserRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(TypesRequest)
class TypesRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(ResponseStatus)
class ResponseStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(WBSubject)
class WBSubjectAdmin(admin.ModelAdmin):
    pass
