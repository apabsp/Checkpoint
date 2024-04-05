from django.contrib import admin
from .models import Game, Profile, Like, Rating

# Register your models here.
admin.site.register(Game)
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Like)
