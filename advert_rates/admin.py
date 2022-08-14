from django.contrib import admin
from advert_rates.models import TelegramUsers, TelegramUsersRequests, TypesRequest, ResponseStatus


@admin.register(TelegramUsers)
class TelegramUsersAdmin(admin.ModelAdmin):
    pass


@admin.register(TelegramUsersRequests)
class TelegramUsersRequestsAdmin(admin.ModelAdmin):
    pass


@admin.register(TypesRequest)
class TypesRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(ResponseStatus)
class ResponseStatusAdmin(admin.ModelAdmin):
    pass

