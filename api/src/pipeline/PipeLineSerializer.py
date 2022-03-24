from rest_framework import serializers
from api.src.pipeline.PipeLineModel import PipeLine


class PipeLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PipeLine
        fields = '__all__'