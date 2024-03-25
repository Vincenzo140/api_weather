from rest_framework.serializers import ModelSerializer
from weather.models import WeatherEntity

class WeatherSerializer(ModelSerializer):
    class Meta:
        model = WeatherEntity;
        fields = '__all__'