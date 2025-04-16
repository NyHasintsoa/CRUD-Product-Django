from django.contrib import admin
from .models import Unite, Category, Product

# Register your models here.

class UniteAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Unites informations", {
            "fields": [
                "unite", "name"
            ],
        }),
    )

    search_fields = ["unite", "name"]
    
    list_display = ('unite', 'name')


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Categories informations", {
            "fields": [
                "category"
            ]
        }),
    )

    search_fields = ["category"]
    
    list_display = ['category']

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Products informations", {
            "fields": [
                "designation", "prixU"
            ]
        }),
        ("Class of the Product", {
            "fields": [
                "unite", "category"
            ]
        }),
    )

    search_fields = ["designation"]
    
    list_display = ('designation', 'prixU', 'unite', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Unite, UniteAdmin)