from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import(authenticate, get_user_model, login, logout,)
from django.shortcuts import render , redirect
from .forms import UserLoginForm, UserSignUpForm
from .models import Profile
from django.views.generic import DetailView

User = get_user_model()

@login_required
def userProfile(request):
    user = request.user
    context = {
        'user': user
    }
    template = 'profile.html'
    return render(request, template, context)





class ProfileView(DetailView):
    template = "profile.html"
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

    def get_context(self):
        context = super(ProfileView, self).get_context(*args, **kwargs)
        return context



#Returns the view for Login.html
#The form context is passed toward UserLoginForm which is located in forms.py
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect("/")

    return render(request, "login.html" , {"form":form})




#Sign up view that passes the from from form.py
def signup_view(request):
    next = request.GET.get('next')
    form = UserSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")


    return render(request, "signup.html",{"form":form})

#Simple logout
def logout_view(request):
    logout(request)
    return redirect("/")
