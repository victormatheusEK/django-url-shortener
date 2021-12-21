from django.contrib.auth import models
from rest_framework import serializers
from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Shortener
        fields = '__all__'
        extra_kwargs = {'owner': {'write_only': True}}
