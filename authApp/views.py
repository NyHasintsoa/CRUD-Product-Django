from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms

# Create your views here.
def home(request) -> HttpResponseRedirect:
    return render(request, "auth/home.html", {
    })

def auth_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Vous vous êtes connecté avec succès !")
                return redirect("product_list")
            else:
                messages.error(request, "Veuillez compléter correctement les champs « nom d’utilisateur » et « mot de passe » d'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse. ")
                return redirect("auth_login")
        else:
            return render(request, "auth/login.html", {
            })
    else:
        messages.success(request, "Vous vous êtes déja connecté")
        return redirect("product_list")
    
def auth_register(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Vous vous êtes inscris avec succès")
            return redirect("product_list")
    else:
        form = forms.SignUpForm()
        return render(request, "auth/register.html", {
            "form" : form,
        })
    return render(request, "auth/register.html", {
            "form" : form,
        })

def auth_logout(request):
    logout(request)
    messages.success(request, "Vous vous êtes déconnecté avec succès")
    return redirect("auth_login")