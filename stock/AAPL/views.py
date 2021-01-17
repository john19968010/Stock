from django.shortcuts import render
from django.http import HttpResponse
from AAPL.models import AAPL
from rest_framework.decorators import action

from rest_framework import viewsets
from AAPL.serializers import AAPLSerializer
# Create your views here.


class AAPLViewset(viewsets.ModelViewSet):
    queryset = AAPL.objects.all()
    serializer_class = AAPLSerializer
    
    def list(self):
        response = super().list
        return a

    # @action(detail=False, action=["get"])
    # def get_info(self, request):
        