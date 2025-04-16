from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="Email address", 
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Email address",
            }
        ),
        error_messages = {
            "required": "Veuillez remplir l'adresse E-mail",
        },
    )
    first_name = forms.CharField(
        label="Firstname",
        max_length="100",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "firstname",
            }
        ),
        error_messages = {
            "required": "Veuillez inclure le prénom",
        },
    )
    last_name = forms.CharField(
        label="Lastname", 
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "lastname",
            }
        ),
        error_messages = {
            "required": "Veuillez inclure votre nom de famille",
        },
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "username",
            }
        ),
        error_messages = {
            "required": "Veuillez entrer votre nom d'utilisateur",
        },
        help_text='<span class="form-text text-muted">Required. 150 characters or fewer</span>'
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "password",
            }
        ),
        error_messages = {
            "required": "Le mot de passe ne doit pas être vide",
        },
        help_text='<span class="form-text text-muted">Your password should be not similar to our personal informations</span>'
    )
    password2 = forms.CharField(
        label="Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "password",
            }
        ),
        error_messages = {
            "required": "La confirmation ne doit pas être vide",
        },
        help_text='<span class="form-text text-muted">Enter the same password as before</span>'
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
