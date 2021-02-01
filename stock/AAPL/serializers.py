from rest_framework import serializers


class PortfolioSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    high = serializers.IntegerField()
    low = serializers.IntegerField()
    open = serializers.IntegerField()
    close = serializers.IntegerField()

class PortfolioResSerializer(serializers.Serializer):
    status = serializers.CharField()
    log = serializers.CharField()
    results = PortfolioSerializer()

class PortfolioReqSerializer(serializers.Serializer):
    stock = serializers.CharField()