from django.urls import path
from . import views
from contacts.views import contact
from vehicles.views import vehicle_list



urlpatterns = [
    path('', views.homePage, name="home"),
    path('other/', views.otherPage, name="other"),
    path('login/', views.logIn, name="login"),
    path('signup/', views.signUp, name="signup"),
    path('dashboard/', views.dashBoard, name="dashboard"),
    path('logout/', views.logOut, name="logout"),
    path('features/', views.featuresPage, name="features"),
    path('contact/', contact, name='contact'),
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('history/', views.history_view, name='history'),
    path('browse/', views.browse_view, name='browse'),
]
