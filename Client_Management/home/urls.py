from django.urls import path
from .views import home
from .views import mylogout

urlpatterns = [
    path('', home, name="home"),
    path('logout/', mylogout, name='logout'),
]