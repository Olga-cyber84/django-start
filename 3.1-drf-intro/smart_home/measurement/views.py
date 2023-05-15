# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement
from django.shortcuts import get_object_or_404


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get("description")
        Sensor.objects.create(name=name, description=description)
        return Response({'name': name, 'description': description})


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get(self, request, pk):
        queryset = Measurement.objects.select_related(
            'sensor').filter(sensor=pk)
        serializer_class = MeasurementSerializer
        return Response(queryset)


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
