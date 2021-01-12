from django.shortcuts import render
from django.http import HttpResponse
from AAPL.models import AAPL
from rest_framework import viewsets
from AAPL.serializers import AAPLSerializer
# Create your views here.


class AAPLViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AAPLSerializer
    
    def aapl(self):
        a = [i for i in range(4)]

        return a