from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError

from .models import User

# Create your views here.
def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "tracker/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))
   





















































def register_view(request):
    if request.method == "GET":
        return render(request, "tracker/register.html")

    else: 
        # Get username, password and email
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        # Check passwords match
        confirmation = request.POST["confirmation"]
        if (password != confirmation):
            return render(request, "tracker/register.html", {
                "message" : "passwords do not match"
            })

        # Add user to datebase
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "tracker/register.html", {
                "message": "email is already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))



def login_view(request):
    if request.method == "GET":
        return render(request, "tracker/login.html")

    else:
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authenticate was successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "tracker/login.html", {
                "message": "Invalid email and/or password"
            })





def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))