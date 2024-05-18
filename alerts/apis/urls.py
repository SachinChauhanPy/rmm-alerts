from django.urls import path
from .views import *

app_name = 'alerts'

urlpatterns = [
    path('categories/',api_categories,name='categories'),
    path('metrics/',api_metrics,name='metrics'),
    path('condition-triggers/',api_condion_triggers,name='condition_triggers'),
    path('condition/',condition,name='condition'),
]
