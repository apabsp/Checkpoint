from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from . import models
from .models import Game
from django.http import JsonResponse

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
        
        return redirect("autenticacao:signin")
    
class SearchView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            context = getUser(req)
            
            searchTerm = req.GET.get("search")

            games = Game.objects.all().filter(name__icontains=searchTerm)

            context["games"] = games

            return render(req, 'app/search.html', context)
        
        return redirect("autenticacao:signin")

class GameView(View):
    def get(self, req, id):
        if(req.user.is_authenticated):
            context = getUser(req)
            
            try:
                game = Game.objects.get(pk=id)
                likes = game.like_set.filter(liked="True")

                context["game"] = game
                try:
                    context["liked"] = "liked" if likes.get(user=req.user).liked else ""
                except:
                    context["liked"] = False

                context["likes"] = len(likes)

                return render(req, 'app/game.html', context)
            except:
                return redirect("app:root")
        
        return redirect("autenticacao:signin")
            
    def post(self, req, id):
        '''like game'''
        if(req.user.is_authenticated):
            try:    
                game = Game.objects.get(pk=id)

                likes = game.like_set.filter(user=req.user)

                if not likes.exists():
                    game.like_set.create(user=req.user, liked=True)
                    game.save()
                else:
                    for like in likes:
                        like.liked = not like.liked
                        like.save()

                like = game.like_set.get(user=req.user)

                return JsonResponse({"message": "Curtiu" if like.liked else "Deixou de curtir"})
            except:
                return JsonResponse({"message": "Jogo nao existe"}, status=404)
            
        return JsonResponse({"message": "Você precisa estar logado"}, status=400)
