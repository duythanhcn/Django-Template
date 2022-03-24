from rest_framework import serializers
from api.src.mansion.MansionModel import Mansion


class MansionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mansion
        fields = '__all__'
