from django.urls import path
from . import views

urlpatterns = [
    # ------------------ Product URL ------------------ #
    path('product/list/', views.product_list, {}, "product_list"),
    path('product/insert/', views.product_insert, {}, "product_insert"),
    path('product/delete/<int:pk>/', views.product_delete, {}, "product_delete"),
    path('product/modify/<int:pk>/', views.product_update, {}, "product_update"),
    # ------------------ Category URL ------------------ #
    path('category/list/', views.category_list, {}, "category_list"),
    path('category/insert/', views.category_insert, {}, "category_insert"),
    path('category/delete/<int:pk>/', views.category_delete, {}, "category_delete"),
    path('category/modify/<int:pk>/', views.category_update, {}, "category_update"),
    # ------------------ Category URL ------------------ #
    path('unite/list/', views.unite_list, {}, "unite_list"),
    path('unite/insert/', views.unite_insert, {}, "unite_insert"),
    path('unite/delete/<int:pk>', views.unite_delete, {}, "unite_delete"),
    path('unite/modify/<int:pk>', views.unite_update, {}, "unite_update"),
]