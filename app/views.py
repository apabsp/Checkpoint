from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from . import models
from .models import Game

def getUser(req):
    user = User.objects.get(username=req.user)
    context = {
        "user": {
            "username": user.username,
            "email": user.email
        }
    }
    return context

class RootView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            context = getUser(req)
            return render(req, 'app/app.html', context)
        
    def _getUser(self, req):
        user = User.objects.get(username=req.user)
        context = {
            "user": {
                "username": user.username,
                "email": user.email
            }
        }
        return context
    
class SearchView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            context = getUser(req)
            
            searchTerm = req.GET.get("search")

            games = Game.objects.all().filter(name__contains=searchTerm)

            context["games"] = games


            games = Game.objects.all().filter(name__contains=searchTerm)

            context["games"] = games

            return render(req, 'app/search.html', context)
        
            return render(req, 'app/search.html', context)

class gamePageView(View):

    #def get(self, req):
    #    context = displayImagem(request,idGame)
    def get(self, req):
        #if(req.user.is_authenticated):
         #   context = displayImagem(req)
         pass

    def displayImagem(request, idGame):
    
        jogoDisplayed = models.Game.objects.get(pk=idGame)
        return render(request, 'gamePage.html', {'game': jogoDisplayed})
    