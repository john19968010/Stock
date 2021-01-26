from django.shortcuts import render
from django.http import HttpResponse
from AAPL.models import AAPL
from rest_framework import viewsets, status
from rest_framework.decorators import action
from AAPL.tasks.dispatch_get_info import get_aapl_info
from rest_framework.response import Response
from datetime import datetime
from AAPL.serializers import AAPLSerializer
import yfinance as yf
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from AAPL.serializers import AAPLResSerializer

class AAPLViewset(viewsets.ModelViewSet):
    queryset = AAPL.objects.all().order_by("date")
    serializer_class = AAPLSerializer
    
    # def list(self):
    #     response = super().list(request, args, kwargs)
    #     return response
    @extend_schema(
        summary="Get current AAPL price",
        responses=AAPLResSerializer,
    )
    @action(detail=False, methods=["get"])
    def get_info(self, request):
        try:
            response = {
                "status" : "FAILURE",
                "log" : ""
            }
            day = datetime.now()
            current_date = f"{day.year}-{day.month}-{day.day-3}"
            current_date_end = f"{day.year}-{day.month}-{day.day-2}"
            print(current_date)
            data = yf.download("AAPL", start=current_date, end=current_date_end)
            dict1 = data.to_dict(orient="index")
            for _, value in dict1.items():
                response["results"] = {}
                response["results"]["date"] = current_date
                response["results"]["open"] = round(value["Open"],1 )
                response["results"]["close"] = round(value["Adj Close"],1 )
                response["results"]["high"] = round(value["High"],1 )
                response["results"]["low"] = round(value["Low"],1 )
            
            # get_aapl_info.delay(day)
            response["status"], response["log"] = "SUCESS", "Get stock_info successful"
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            if str(e) == "DataFrame index must be unique for orient='index'.":
                response["log"] = "The date is in weekend or market havn't open yet"
                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            response["log"] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

