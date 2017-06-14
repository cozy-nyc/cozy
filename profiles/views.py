from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from .forms import UserLoginForm


@login_required
def userProfile(request):
    user = request.user
    context = {
        'user': user
    }
    template = 'profile.html'
    return render(request, template, context)

#Returns the view for Login.html
#The form context is passed toward UserLoginForm which is located in forms.py
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

    return render(request, "login.html" , {"form":form})




#Empty Not in use yet
def register_view(request):
    return render('more memes')

#Empty Not in use yet
def logout_view(request):
    return render('even MORE memes')
