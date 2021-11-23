from rest_framework import serializers

from firstApp.models import CarSpecs


class CarSpecsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['id', 'car_brand', 'car_model', 'production_year', 'car_body', 'engine_type']