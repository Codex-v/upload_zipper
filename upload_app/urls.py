# upload_app/urls.py
from django.urls import path
from .views import upload

urlpatterns = [
    path('', upload, name='upload'),
]
