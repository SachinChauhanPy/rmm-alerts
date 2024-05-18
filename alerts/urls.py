from django.urls import path
from .views import *

app_name = 'alerts'

urlpatterns = [
    path('',alerts_view,name='alerts'),
]
