from django.urls import path,include
from django.conf.urls import url
from . import views
from .views import index


urlpatterns = [
    url('index',index.as_view()),
]