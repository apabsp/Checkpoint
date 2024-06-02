from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):
    name = models.CharField(max_length=50) #A API tem q mandar pra esse models ok?
    image = models.CharField(max_length=200, default=False)
    platforms = models.JSONField(default=dict)
    screenshots = models.JSONField(default=dict)
    

    def __str__(self) -> str:
        return self.name
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.username + " - " + self.game.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    image = models.CharField(max_length=2000, default="")
    wishList = models.ManyToManyField(Game, related_name='wishlist')
    favorites = models.ManyToManyField(Game, related_name='Favorites')

    def __str__(self) -> str:
        return self.user.username


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    nota = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self) -> str:
        return self.user.username + " - " + self.game.name + " - " + str(self.nota)


class Review(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   game = models.ForeignKey(Game, on_delete=models.CASCADE)
   text = models.TextField(max_length=10000, default="minha Review legal!")
   likes = models.IntegerField(default=0)
   liked_by = models.ManyToManyField(User, related_name='liked_reviews')

   def __str__(self) -> str:
        return self.user.username + " - " + self.game.name
   
   