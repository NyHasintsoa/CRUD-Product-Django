from django.db import models
from django.urls import reverse

# Create your models here.

class Unite(models.Model):
    unite = models.CharField(max_length=60, unique=True, null=False)
    name = models.CharField(max_length=110, unique=True, null=True)

    class Meta:
        verbose_name = ("unite")
        verbose_name_plural = ("unites")

    def __str__(self):
        return self.unite
    
    def get_absolute_url(self):
        return reverse("unite_detail", kwargs={"pk": self.pk})
    

class Category(models.Model):
    category = models.CharField(max_length=60, unique=True, null=False)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse("unite_detail", kwargs={"pk": self.pk})
    

class Product(models.Model):
    designation = models.CharField(max_length=60, unique=True, null=False)
    prixU = models.IntegerField(null=False, default=100)
    unite = models.ForeignKey("Unite", on_delete=models.PROTECT, null=False)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=False)

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return (f"{self.designation} {self.prixU}")
    
    def get_absolute_url(self):
        return reverse("unite_detail", kwargs={"pk": self.pk})