from django.contrib import admin
from .models import Product
from .models import General
from .models import Time


# Register your models here.
admin.site.register(Product)
admin.site.register(General)
admin.site.register(Time)