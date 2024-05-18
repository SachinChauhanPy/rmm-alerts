from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class MetricCategory(models.Model):
    name = models.CharField(verbose_name='Metric Category Name', max_length=50)
    
    def __str__(self):
        return self.name

class Metric(models.Model):
    category = models.ForeignKey(MetricCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parameters = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name
    
class ConditionTrigger(models.Model):
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    conditions = models.JSONField(default=list) 
    
    def __str__(self):
        return self.metric.name
    
""" 
Email Alert
Run Script
Run Task
"""
class AlertAction(models.Model):
    name = models.CharField(max_length=255)
    
class Condition(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    alert_description = models.CharField(verbose_name='Alert Description', max_length=255)
    configuration = models.JSONField(default=dict)
    
    def __str__(self):
        return self.alert_description

class Alert(models.Model):
    duration = models.DecimalField(
        'Duration (minutes)',
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(1440)],
        default=2,
        null=True,
        blank=True
        )
    conditions = models.ManyToManyField(Condition)
    realtime_status = models.BooleanField(default=True)