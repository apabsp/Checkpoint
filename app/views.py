from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from . import models
from .models import Game, Review
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
        if req.user.is_authenticated:
            context = getUser(req)
            try:
                game = Game.objects.get(pk=id)
                likes = game.like_set.filter(liked=True)
                review = game.review_set.filter(user=req.user)

                allReviews = game.review_set.all().exclude(user=req.user)

                context["allReviews"] = allReviews

                if(review.exists()):
                    context["review"] = review.first()

                
                context["game"] = game

                try:
                    context["liked"] = "liked" if likes.get(user=req.user).liked else ""
                except:
                    context["liked"] = False

                context["likes"] = len(likes)
                
               
                try:
                    user_review = Review.objects.get(user=req.user, game=game)
                    context["user_review"] = user_review.text
                except Review.DoesNotExist:
                    context["user_review"] = None
                return render(req, 'app/game.html', context)
            except Exception as e:
                print("An error occurred:", e)
                return redirect("app:root")
        
        return redirect("autenticacao:signin")

    def post(self, req, id):
        if req.POST.get("action") == "submit_review":
            return self.criandoReview(req, id)
        else:
            return self.like_game(req, id)

    def like_game(self, req, id):
        if req.user.is_authenticated:
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
                return JsonResponse({"message": "Jogo não existe"}, status=404)
        else:
            return JsonResponse({"message": "Você precisa estar logado"}, status=400)

    def criandoReview(self, req, id):
        if req.user.is_authenticated:
            try:
                game = Game.objects.get(pk=id)
                review_text = req.POST.get('textoDaReview')

                existing_review = Review.objects.filter(user=req.user, game=game).first()

                if existing_review:
                    existing_review.text = review_text
                    existing_review.save()
                    return redirect(f"/app/review/{existing_review.id}")
                
                else:
                    novaReview = Review(user=req.user, game=game, text=review_text)
                    novaReview.save()

                    return redirect(f"/app/review/{novaReview.id}")
            except Game.DoesNotExist:
                return JsonResponse({"message": "Jogo não encontrado"}, status=404)
            
        else:
            return JsonResponse({"message": "Você precisa estar logado"}, status=400)


class ReviewView(View):
    def get(self, req, id):
        if(req.user.is_authenticated):
            context = getUser(req)

            try:
                review = Review.objects.get(pk=id)
                game = review.game
                print(game);

                context["game"] = game
                context["review"] = review

                return render(req, "app/review.html", context)
            except:
                return redirect("app:root")
            
        return redirect("app:root")