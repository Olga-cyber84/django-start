from rest_framework import serializers
from .models import Measurement, Sensor

# для создания нового датчика / изменения 
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


#для добавления измерений
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

#для получения информации по одному датчику
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(source='sensors', read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

