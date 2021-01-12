from django.contrib.auth.models import AAPL
from rest_framework import serializers

class AAPLSerializer(serializers.Serializers):
    date = serializers.DateTimeField()
    high = serializers.IntegerField()
    low = serializers.IntegerField()
    open = serializers.IntegerField()
    close = serializers.IntegerField()