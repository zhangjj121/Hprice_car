from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserInfo)
admin.site.register(DetailInfo)
admin.site.register(Bank)
admin.site.register(Message)