from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from .models import Game, Review
from django.http import JsonResponse
import json

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
                rates = game.rating_set.filter(user=req.user)
                review = game.review_set.filter(user=req.user)

                allReviews = game.review_set.all().exclude(user=req.user)

                context["allReviews"] = allReviews

                if(rates.exists()):
                    context["rate"] = rates[0]

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
        
        typeAction = json.loads(req.body)["type"]
        
        if typeAction == "liking":
            return self.likeGame(req, id)
        
        elif typeAction == "rating":
            nota = json.loads(req.body)["nota"]
            return self.rateGame(req, id, nota)

    def rateGame(self, req, id, nota):
        if req.user.is_authenticated:
            try:
                game = Game.objects.get(pk=id)
                rates = game.rating_set.filter(user=req.user)

                if not rates.exists():
                    game.rating_set.create(user=req.user, nota=nota)
                    game.save()
                else:
                    for rate in rates:
                        rate.nota = nota
                        rate.save()

                return JsonResponse({"message": "Avaliou"})
            except:
                return JsonResponse({"message": "Jogo não existe"}, status=404)
        else:
            return JsonResponse({"message": "Você precisa estar logado"}, status=400)

    def likeGame(self, req, id):
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
                reviewCreator = review.user

                context["game"] = game
                context["review"] = review
                context["reviewCreator"] = reviewCreator

                return render(req, "app/review.html", context)
            except:
                return redirect("app:root")
            
        return redirect("app:root")
    

    def post(self, req, id):
        if req.user.is_authenticated:

            action = req.POST.get("action")

            if action == "delete":
                return self.delete_post(id=id)
            elif action == "edit":
                return self.edit_post(req=req, id=id)

        return redirect("app:root")
    

    def edit_post(self, req, id):
        try:
            toEdit = Review.objects.get(pk=id)
            toEdit.text = req.POST.get("review-text")
            toEdit.save()

            messages.add_message(req, constants.SUCCESS, "Review alterado com sucesso!")
            
            return redirect("app:review", id=id)
        except Exception as e:
            print(e)
            return redirect("app:root")


    def delete_post(self, id):
        try:
            toDelete = Review.objects.get(pk=id)
            toDelete.delete()
            
            return redirect("app:game", id=toDelete.game.id)
        except Exception as e:
            print(e)
            return redirect("app:root")