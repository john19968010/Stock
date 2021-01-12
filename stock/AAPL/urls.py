from django.urls import path

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
routers.register(r'AAPL',views.AAPLViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('aapl/', include('rest_framework.urls', namespace='aapl'))
]
]