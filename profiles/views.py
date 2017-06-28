from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db import transaction

User = get_user_model()


class ProfileView(DetailView):
    template = "profile.html"
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context(self):
        context = super(ProfileView, self).get_context(*args, **kwargs)
        return context

