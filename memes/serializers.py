# todos/serializers.py
from rest_framework import serializers
from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        	'id',
            'name',
            'url',
            'caption',
        )
        model = Meme