from django.urls import path
from .views import jannat
urlpatterns = [
    path('', jannat),
]