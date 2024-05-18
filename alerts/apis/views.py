from alerts.models import *

from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET',])
def api_categories(request):
    categories = MetricCategory.objects.all()
    serializers = MetricCategorySerializer(categories,many=True)
    return Response(serializers.data)

@api_view(['GET',])
def api_metrics(request):
    catid = request.GET.get('catid')
    metrics = Metric.objects.filter(category__id=catid)
    serializers = MetricSerializer(metrics,many=True)
    return Response(serializers.data)

@api_view(['GET',])
def api_condion_triggers(request):
    mid = request.GET.get('mid')
    metrics = ConditionTrigger.objects.get(metric__id=mid)
    serializers = ConditionTriggerSerializer(metrics)
    return Response(serializers.data)

@api_view(['GET','POST','PUT','DELETE'])
def condition(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        if cid:
            condition = Condition.objects.get(unique_id=cid)
            serializer = ConditionSerializer(condition)
            return Response(serializer.data)
        else:
            conditions = Condition.objects.all()
            if conditions:
                serializer = ConditionSerializer(conditions,many=True)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        serializer = ConditionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        try:
            condition = Condition.objects.get(unique_id=request.data['unique_id'])
        except Condition.DoesNotExist:
            return Response({'error': 'Condition not found'}, status=status.HTTP_404_NOT_FOUND)
        partial_data = {
            'alert_description':request.data.get('alert_description'),
            'configuration': request.data.get('configuration')
        }
        serializer = ConditionSerializer(condition, data=partial_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            condition_id = request.data['unique_id']
            condition = Condition.objects.get(unique_id=condition_id)
        except Condition.DoesNotExist:
            return Response({'error': 'Condition not found'}, status=status.HTTP_404_NOT_FOUND)
        
        condition.delete()
        return Response({'message': 'Condition deleted successfully'}, status=status.HTTP_204_NO_CONTENT)