

from django.conf.urls import url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/',views.index, name="index"),
    url(r'^message/',views.Message.as_view(), name="message"),
]
