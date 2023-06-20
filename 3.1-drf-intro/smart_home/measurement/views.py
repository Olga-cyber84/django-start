from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer
from .models import Sensor, Measurement


class SensorView(ListCreateAPIView): #создание датчика / вывод списка
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get("description")
        Sensor.objects.create(name=name, description=description)
        return Response({'name': name, 'description': description})


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        one_sensor = Sensor.objects.get(id=pk)
        name_default = one_sensor.name
        description_default = one_sensor.description
        one_sensor.name = request.data.get('name', name_default)
        one_sensor.description = request.data.get('description', description_default)
        one_sensor.save()
        return Response({"status": "sensor's info updated"})

class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
