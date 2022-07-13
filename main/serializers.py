from rest_framework import serializers

from .models import shortUrl


class shortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = shortUrl
        fields = ('longUrl','shortUrl','time')
        