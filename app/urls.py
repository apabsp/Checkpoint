from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.AppView.as_view(), name='signin'),
]