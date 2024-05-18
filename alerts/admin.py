from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(MetricCategory)
class MetricCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ['category','name','parameters']
    
@admin.register(ConditionTrigger)
class ConditionTriggerAdmin(admin.ModelAdmin):
    list_display = ['metric','conditions']
    
@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['unique_id','configuration']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['duration','realtime_status']
    
@admin.register(AlertAction)
class AlertActionAdmin(admin.ModelAdmin):
    list_display = ['name',]