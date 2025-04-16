from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Product, Unite, Category
from . import forms

# ---------------------------------------------
#   Product Views
# ---------------------------------------------
def product_list(request) -> HttpResponseRedirect:
    if request.user.is_authenticated:
        products = Product.objects.all()
        if request.method == "GET":
            param = request.GET.get("q") or ""
            if param != "":
                products = products.filter(designation__contains=param)
        getPage = int(request.GET.get("page") or 1)
        pagination = Paginator(object_list=products, per_page=5)
        productsPerPage = pagination.page(getPage)
        nextPage = 0
        previousPage = 0
        if productsPerPage.has_next() :
            nextPage = productsPerPage.next_page_number()
        if productsPerPage.has_previous() :
            previousPage = productsPerPage.previous_page_number()
        return render(request, "products/index.html", {
            "products" : productsPerPage,
            "count" : products.count(),
            "search" : True,
            "value" : param,
            "pagination" : pagination,
            "nextPage" : nextPage,
            "previousPage" : previousPage,
            "getPage" : getPage,
        })
    else:
        messages.error(request, "Vous devez vous connecté pour accédé à cette page")
        return redirect("auth_login")

    
def product_delete(request, pk):
    if request.user.is_authenticated:
        Product.objects.get(id=pk).delete()
        messages.success(request, "Produit supprimer avec succès")
        return redirect("product_list")
    else:
        messages.error(request, "Vous devez vous connecté pour supprimer un produit")
        return redirect("auth_login")
    
def product_update(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(id=pk)
        form = forms.ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit modifier avec succès")
            return redirect("product_list")
        return render(request, "products/update.html", {
            "form" : form,
            "product" : product
        })
    else:
        messages.error(request, "Vous devez vous connecté pour modifier un produit")
        redirect("auth_login")

def product_insert(request):
    if request.user.is_authenticated:
        form = forms.ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouter avec succès")
            return redirect("product_insert")
        return render(request, "products/insert.html", {
            "form" : form
        })
    else:
        messages.error(request, "Vous devez vous connecter pour ajouter des produits")
        redirect("auth_login")


# ---------------------------------------------
#   Category Views
# ---------------------------------------------
def category_list(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        if request.method == "GET" :
            param = request.GET.get("q") or ""
            if param != "":
                categories = categories.filter(category__contains=param)
        return render(request, "categories/index.html", {
            "categories" : categories,
            "count" : categories.count(),
            "search" : True,
            "value" : param
        })
    else:
        messages.error(request, "Vous devez vous connecté pour accéder à cette page")
        return redirect("auth_login")

def category_delete(request, pk):
    if request.user.is_authenticated:
        Category.objects.get(id=pk).delete()
        messages.success(request, "Catégorie supprimer avec succès")
        return redirect("category_list")
    else:
        messages.error(request, "Vous devez vous connecter pour supprimer cette catégorie")
        return redirect("auth_login")

def category_update(request, pk):
    if request.user.is_authenticated:
        category = Category.objects.get(id=pk)
        form = forms.CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Catégorie modifier avec succès")
            return redirect("category_list")
        return render(request, "categories/update.html", {
            "form" : form,
            "category" : category
        })
    else:
        messages.error(request, "Vous devez vous connecter pour modifier des catégories")
        redirect("auth_login")

def category_insert(request):
    if request.user.is_authenticated:
        form = forms.CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Catégorie ajouter avec succès")
            return redirect("category_list")
        return render(request, "categories/insert.html", {
            "form" : form
        })
    else:
        messages.error(request, "Vous devez vous connecter pour ajouter des catégories")
        redirect("auth_login")


# ---------------------------------------------
#   Unite Views
# ---------------------------------------------
def unite_list(request):
    if request.user.is_authenticated:
        unites = Unite.objects.all()
        if request.method == "GET":
            param = request.GET.get("q") or ""
            if param != "" :
                unites = unites.filter(name__contains=param)
        return render(request, "unites/index.html", {
            "unites" : unites,
            "count" : unites.count(),
            "search" : True,
            "value" : param
        })
    else:
        messages.error(request, "Vous devez vous connecté pour accéder à cette page")
        return redirect("auth_login")

def unite_delete(request, pk):
    if request.user.is_authenticated:
        Unite.objects.get(id=pk).delete()
        messages.success(request, "Unité supprimer avec succès")
        return redirect("unite_list")
    else:
        messages.error(request, "Vous devez vous connecter pour supprimer cette unité")
        return redirect("auth_login")
    
def unite_update(request, pk):
    if request.user.is_authenticated:
        unite = Unite.objects.get(id=pk)
        form = forms.UniteForm(request.POST or None, instance=unite)
        if form.is_valid():
            form.save()
            messages.success(request, "Unité modifier avec succès")
            return redirect("unite_list")
        return render(request, "unites/update.html", {
            "form" : form,
            "unite" : unite
        })
    else:
        messages.error(request, "Vous devez vous connecter pour modifier une unité")
        redirect("auth_login")

def unite_insert(request):
    if request.user.is_authenticated:
        form = forms.UniteForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Unité ajouter avec succès")
            return redirect("unite_list")
        return render(request, "unites/insert.html", {
            "form" : form
        })
    else:
        messages.error(request, "Vous devez vous connecter pour ajouter une unité")
        redirect("auth_login")