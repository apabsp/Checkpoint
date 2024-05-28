from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from .models import Game, Review, Profile
from django.http import JsonResponse
import json
import math

def getUser(req):
    user = User.objects.get(username=req.user)
    context = {
        "user": {
            "username": user.username,
            "email": user.email,
            "userId": user
        }
    }
    return context

class RootView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            context = getUser(req)
            
            games = Game.objects.all()

            trendingGames = []
            restGames = []

            for game in games:
                rates = game.rating_set.all()
                ratesSum = 0
                for rate in rates:
                    ratesSum += rate.nota

                avgRates = ((ratesSum / len(rates)) * 2 * 10) if len(rates) > 0 else 0

                if(avgRates == 0):
                    restGames.append(game)
                    continue

                trendingGames.append({
                    "game": game,
                    "avgRate": math.ceil(avgRates)
                })

            trendingGames.sort(key=lambda g: g["avgRate"], reverse=True)

            context["trendings"] = trendingGames
            context["games"] = restGames

            return render(req, 'app/app.html', context)
        
        return redirect("autenticacao:signin")


def searchGame(wishList, game):
    for index, objeto in enumerate(wishList):
        if objeto.name == game.name:
            return index

    return None


class SearchView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            user = User.objects.get(username=req.user)

            context = {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "userId": user,
                }
            }

            try:
                profile = Profile.objects.get(user=user)

            except:
                profile = Profile.objects.create(user=user)
                profile.save()
                
            
            searchTerm = req.GET.get("search")

            games = Game.objects.all().filter(name__icontains=searchTerm)

            wishList = profile.wishList.all()

            context["games"] = []

            for game in games:
                index = searchGame(wishList, game)
                
                context["games"].append({
                    "id": game.id,
                    "name": game.name,
                    "image": game.image,
                    "onWishlist": True if index != None else False 
                })

            context["searchParams"] = searchTerm

            return render(req, 'app/search.html', context)
        
        return redirect("autenticacao:signin")
    
    def post(self, req):
        if(req.user.is_authenticated):
            user = User.objects.get(username=req.user)

            context = {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "userId": user,
                }
            }
            
            searchTerm = req.POST.get("searchParams")
            gameName = req.POST.get("currentGame")
            action = req.POST.get("action")

            games = Game.objects.all().filter(name__icontains=searchTerm)
            game = Game.objects.all().filter(name=gameName)[0]

            try:
                profile = Profile.objects.get(user=user)
                if(game):
                    if(action == "add"):
                        profile.wishList.add(game)
                    else:
                        profile.wishList.remove(game)

                profile.save()

            except:
                profile = Profile.objects.create(user=user)
                if(game):
                    if(action == "add"):
                        profile.wishList.add(game)
                    else:
                        profile.wishList.remove(game)
                    
                profile.save()


            wishList = profile.wishList.all()

            context["games"] = []

            for game in games:
                index = searchGame(wishList, game)
                
                context["games"].append({
                    "id": game.id,
                    "name": game.name,
                    "image": game.image,
                    "onWishlist": True if index != None else False 
                })

            context["searchParams"] = searchTerm

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
            texto_da_review = req.POST.get("textoDaReview")
            if texto_da_review == "" or texto_da_review.isspace():
                messages.add_message(req, constants.SUCCESS, "Review está vazia! Digite algo!")
                return redirect("app:game", id=id)
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
                return self.delete_post(req=req, id=id)
            elif action == "edit":
                return self.edit_post(req=req, id=id)
            elif action == "like":
                print("Exactly as planned!!")
                return self.like_post(req=req, id=id)

        return redirect("app:root")
    

    def edit_post(self, req, id):
        try:
            toEdit = Review.objects.get(pk=id)
            toEdit.text = req.POST.get("review-text")
            if toEdit.text == "" or toEdit.text.isspace():
                messages.add_message(req, constants.SUCCESS, "Por favor, insira um texto válido!")
                return redirect("app:review", id=id)
            toEdit.save()

            messages.add_message(req, constants.SUCCESS, "Review alterada com sucesso!")
            
            return redirect("app:review", id=id)
        except Exception as e:
            print(e)
            return redirect("app:root")

    def like_post(self, req, id):
        try: 
            toLike = Review.objects.get(pk=id)
            username = getUser(req)["user"]["username"]
            user = User.objects.get(username=username)

            
            if user in toLike.liked_by.all():
                #if it has already been liked, unlike it
                toLike.liked_by.remove(user)
                toLike.likes -= 1
                messages.add_message(req, constants.SUCCESS, "Você descurtiu esta Review!")
            else:
                toLike.liked_by.add(user)
                toLike.likes += 1
                messages.add_message(req, constants.SUCCESS, "Você curtiu esta Review!")
            #print("am I getting here?")
            toLike.save()
            print(f"user é isso{user}\n{Review.liked_by} all liked by é isso")
            return redirect("app:review", id=id)
        except Exception as e: #
            print(e)
            return redirect("app:root")
        
    def delete_post(self, req, id):
        try:
            toDelete = Review.objects.get(pk=id)
            toDelete.delete()
            
            messages.add_message(req, constants.SUCCESS, "Review deletada com sucesso!")

            return redirect("app:game", id=toDelete.game.id)
        except Exception as e:
            print(e)
            return redirect("app:root")
        

class ProfileView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            user = User.objects.get(username=req.user)

            try:
                profile = Profile.objects.get(user=user)

            except:
                profile = Profile.objects.create(user=user)
                    
                profile.save()

            context = {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "userId": user,
                    "image": profile.image
                }
            }

            context["wishlist"] = profile.wishList.all()

            return render(req, 'app/profile.html', context)
        
        return redirect("autenticacao:signin")
    
    def post(self, req):
        if(req.user.is_authenticated):
            imageUrl = req.POST.get("url")

            user = User.objects.get(username=req.user)

            try:
                profile = Profile.objects.get(user=user)
                profile.image = imageUrl
                profile.save()

            except:
                profile = Profile.objects.create(user=user, image=imageUrl)
                    
                profile.save()

            context = {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "userId": user,
                    "image": profile.image
                }
            }

            context["wishlist"] = profile.wishList.all()

            return render(req, 'app/profile.html', context)
        
        return redirect("autenticacao:signin")