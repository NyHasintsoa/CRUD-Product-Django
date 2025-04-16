from django import forms
import random
from .models import Product, Unite, Category

# ---------------------------------------------
#   Product Form
# ---------------------------------------------
class ProductForm(forms.ModelForm):
    designation = forms.CharField(
        label="Désignation",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
            }
        ),
        error_messages= {
            "required" : "Veuillez donner un nom au produit !"
        }
    )
    prixU = forms.IntegerField(
        label="Prix unitaire",
        widget=forms.NumberInput(
            attrs={
                "class" : "form-control",
            }
        )
    )
    
    class Meta:
        model = Product
        fields = ('designation', 'prixU', 'unite', 'category')


# ---------------------------------------------
#   Category Form
# ---------------------------------------------
class CategoryForm(forms.ModelForm):
    category = forms.CharField(
        label="Categorie",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control"
            }
        ),
        error_messages= {
            "required" : "Veuillez remplir la zone de saisie, s'il vous plaît !"
        }
    )

    class Meta:
        model = Category
        fields = ["category"]


# ---------------------------------------------
#   Unite Form
# ---------------------------------------------
class UniteForm(forms.ModelForm):
    unite = forms.CharField(
        label="Unité Produit",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control"
            }
        ),
        error_messages= {
            "required" : "Veuillez remplir la zone de saisie, s'il vous plaît !"
        }
    )
    name = forms.CharField(
        label="Nom de l'unité",
        widget=forms.TextInput(
            attrs={
                "class" : "form-control"
            }
        ),
        error_messages= {
            "required" : "Veuillez remplir la zone de saisie, s'il vous plaît !"
        }
    )
    class Meta:
        model = Unite
        fields = ("unite", "name")
