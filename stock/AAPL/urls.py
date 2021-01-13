from django.urls import path,include
from rest_framework import routers
from AAPL.views import AAPLViewset

router = routers.DefaultRouter()
router.register(r"AAPL", AAPLViewset)


urlpatterns = [
    path('', include(router.urls)),
    # path('aapl/', include('rest_framework.urls', namespace='aapl'))

]


