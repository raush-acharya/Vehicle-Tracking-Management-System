from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('other/', views.otherPage, name="other"),
    path('login/', views.logIn, name="login"),
    path('signup/', views.signUp, name="signup"),
    path('dashboard/', views.dashBoard, name="dashboard"),
    path('logout/', views.logOut, name="logout"),
    path('features/', views.featuresPage, name="features"),
]
