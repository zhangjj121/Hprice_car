from django.contrib import admin

# Register your models here.
from buy.models import *

admin.site.register(Cart)
admin.site.register(Order)