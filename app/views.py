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
                
                context["game"] = game
                print("DID I GET HERE???")

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
                    return JsonResponse({"message": "Review atualizada!"})
                else:
                    novaReview = Review(user=req.user, game=game, text=review_text)
                    novaReview.save()
                    return JsonResponse({"message": "Review adicionada!"})
            except Game.DoesNotExist:
                return JsonResponse({"message": "Jogo não encontrado"}, status=404)
        else:
            return JsonResponse({"message": "Você precisa estar logado"}, status=400)



        
        # if req.user.is_authenticated:
        #     print("hello am I authenticated?")
        #     try:
        #         game = Game.objects.get(pk=id)
        #         review_text = req.POST.get('textoDaReview')


        #         novaReview = models.Review(user = req.user, game = Game.objects.get(pk=id), text = review_text)
        #         if len(novaReview.objects.all()):      
        #             novaReview.objects.all().delete()
        #             #fiz uma gambiarra aqui pra garantir que só fique uma review por usuário
        #         novaReview.save()

        #         return JsonResponse({"message": "Review adicionada!"})
        #     except Game.DoesNotExist:
        #         print("jogo não encontrado")
        #         return JsonResponse({"message": "Jogo nao existe"}, status=404)
        # else:
        #     return JsonResponse({"message": "Você precisa estar logado"}, status=400)

    # class GameView(View):
    #     def get(self, req, id):
    #         # Fetch the game object
    #         game = Game.objects.get(pk=id)
            
    #         # Fetch the review associated with the current user and the game
    #         user_review = None
    #         if req.user.is_authenticated:
    #             user_review = models.Review.objects.filter(user=req.user, game=game).first()
            
    #         # Pass the game and user's review to the template context
    #         context = {
    #             'game': game,
    #             'user_review': user_review,
    #         }
    #         return render(req, 'app/game.html', context)