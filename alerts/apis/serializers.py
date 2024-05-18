from rest_framework.serializers import ModelSerializer
from alerts.models import *

class MetricCategorySerializer(ModelSerializer):
    class Meta:
        model = MetricCategory
        fields = '__all__'
        
class MetricSerializer(ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'
        
class ConditionTriggerSerializer(ModelSerializer):
    class Meta:
        model = ConditionTrigger
        fields = '__all__'
        depth = 2
        
class ConditionSerializer(ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'