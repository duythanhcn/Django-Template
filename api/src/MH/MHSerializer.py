from rest_framework import serializers
from api.src.MH.MHModel import MH


class MHSerializer(serializers.ModelSerializer):

    class Meta:
        model = MH
        fields = '__all__'
