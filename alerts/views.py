from django.shortcuts import render
from django.middleware.csrf import get_token
from .models import *
# Create your views here.

def alerts_view(request):
    metric_types = MetricCategory.objects.all()
    actions = AlertAction.objects.all()
    csrf_token = get_token(request)
    context = {
        'metric_types':metric_types,
        'actions':actions,
        'csrf_token': csrf_token
    }
    return render(request,'alerts.html',context)