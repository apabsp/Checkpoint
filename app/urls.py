from django.urls import path
from . import views
from . import populate_view

app_name = 'app'

urlpatterns = [
    path('', views.RootView.as_view(), name='root'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('game/<int:id>/', views.GameView.as_view(), name='game'),
    path('review/<int:id>/', views.ReviewView.as_view(), name='review'),
    path('populate/', populate_view.populate, name='populate'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]