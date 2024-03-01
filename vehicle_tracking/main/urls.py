from django.urls import path
from . import views
from .views import otherPage

urlpatterns = [
    path('', views.taskList, name="home"),
    path('other/', otherPage, name="other"),
]
