# from django.contrib import admin
# from .models import *
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
#
#
# class UserInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'Доп. информация'
#
#
# # Определяем новый класс настроек для модели User
# class UserAdmin(UserAdmin):
#     inlines = (UserInline,)
#
#
# # Перерегистрируем модель User
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
#

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Technic)
class TechnicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


@admin.register(DrivingBridge)
class DrivingBridgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


@admin.register(ControlledBridge)
class ControlledBridgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    filter = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'car_number',
        'technic',
        'engine',
        'transmission',
        'driving_bridge',
        'controlled_bridge',
        'date_shipment',
        'equipment',
        'client',
        'service_company',
    )
    filter = ('car_number',)
