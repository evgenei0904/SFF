from django.contrib import admin
from .models import *


@admin.register(TypeMaintenance)
class TypeMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id','name','description',)
    filter = ('name',)


@admin.register(Failure)
class FailureAdmin(admin.ModelAdmin):
    list_display = ('id','name','description',)
    filter = ('name',)


@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ('id','name','description',)
    filter = ('name',)


@admin.register(ServiceCompany)
class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name','description',)
    filter = ('name',)


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id','type','date','operating_time','order_number','order_date','service_company','car')
    filter = ('date',)


@admin.register(Complaint)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('id','date_failure','operating_time','node_failure','date_recovery','downtime','car','service_company')
    filter = ('date_failure',)
