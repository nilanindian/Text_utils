from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("",views.home,name="home"),
    path("analyze",views.analyze,name="analyze")
]
