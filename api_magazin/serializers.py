from rest_framework import serializers

from .models import City, Street, Magazine


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name', 'city']


class ShopSerializer(serializers.ModelSerializer):

    street = serializers.SlugRelatedField(read_only=True, slug_field='name')
    city = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Magazine
        fields = '__all__'
