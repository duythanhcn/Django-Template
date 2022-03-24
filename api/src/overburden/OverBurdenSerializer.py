from rest_framework import serializers
from api.src.overburden.OverBurdenModel import OverBurden


class OverBurdenSerializer(serializers.ModelSerializer):

    class Meta:
        model = OverBurden
        fields = '__all__'
