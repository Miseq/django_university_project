from rest_framework import serializers

from .models import Place


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('PlaceID', 'Name', 'Description', 'IconURL', 'Latitude', 'Longitude',)
