from rest_framework import serializers


class AAPLSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    high = serializers.IntegerField()
    low = serializers.IntegerField()
    open = serializers.IntegerField()
    close = serializers.IntegerField()

class AAPLResSerializer(serializers.Serializer):
    status = serializers.CharField()
    log = serializers.CharField()
    results = AAPLSerializer()
