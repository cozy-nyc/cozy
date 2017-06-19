
from django.contrib.auth.decorators import login_required
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.shortcuts import render , redirect
from .forms import UserLoginForm, UserSignUpForm
from .models import Profile
from django.views.generic import DetailView


User = get_user_model()


class ProfileView(DetailView):
    template = "profile.html"
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context(self):
        context = super(ProfileView, self).get_context(*args, **kwargs)
        return context
