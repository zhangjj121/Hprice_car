from django.conf.urls import url

from userinfo.views import *

urlpatterns = [
    url(r'^register/$',register)
]