from django.contrib import admin
from .models import AAPL, BuyRecord
# Register your models here.

admin.site.register(AAPL)
admin.site.register(BuyRecord)