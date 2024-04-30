from django.urls import path
from apps.views import index, home, about

urlpatterns = [
    path("", home, name="home"),
    path("index", index, name="index"),
    path("about", about, name="about")

]
