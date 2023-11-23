from django.urls import path, include
from .views import ListPerson, CreatePerson

urlpatterns = [
    path("", ListPerson.as_view(), name='main'),
    path("create/", CreatePerson.as_view(), name='create'),
]

