from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement:
    id = models.IntegerField(primary_key=True)
    temperature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
