from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
class RootView(View):
    def get(self, req):
        if(req.user.is_authenticated):
            context = self._getUser(req)
            return render(req, 'app/app.html', context)
        
    def post(self, req):
        if(req.user.is_authenticated):
            context = self._getUser(req)
            search = req.POST.get("search")
            print(search)
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
            context = self._getUser(req)
            
            searchTerm = req.GET.get("search")

            return render(req, 'app/search.html', context)
        
    def _getUser(self, req):
        user = User.objects.get(username=req.user)
        context = {
            "user": {
                "username": user.username,
                "email": user.email
            }
        }
        return context