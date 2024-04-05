from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.RootView.as_view(), name='root'),
    path('search/', views.SearchView.as_view(), name='search'),
]