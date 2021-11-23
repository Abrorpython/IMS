from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from firstApp.models import CarSpecs
from .serializers import CarSpecsSerializers


@api_view()
@permission_classes([AllowAny])
def firstRequest(request):
    print(request.query_params)
    return Response({
        "salom": "Salomcha"
    })


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializers

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        cars = CarSpecs.objects.filter(car_brand=params['pk'])
        serializer = CarSpecsSerializers(cars, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data                                         # kiritilgan ma`lumotlarni qaytishi

        new_car = CarSpecs.objects.create(car_brand=car_data['car_brand'], car_model=car_data['car_model'],
        production_year=car_data['production_year'], car_body=car_data['car_body'],
        engine_type=car_data['engine_type'])

        new_car.save()

        serializer = CarSpecsSerializers(new_car)

        return Response(serializer.data)

