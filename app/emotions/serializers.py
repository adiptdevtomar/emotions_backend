from rest_framework import serializers
from emotions import models


class EmotionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmotionModel
        fields = ['text']