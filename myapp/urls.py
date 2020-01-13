from django.urls import path
from myapp import views
urlpatterns = [
    path('<id>/',views.index,name="index"),
]
