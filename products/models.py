from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile


class Category(models.Model):
    """models for category in product app, just names"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """relevant fields for product models in product app"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """relevant fields for comment models in product app"""
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=250, null=True)
    posted_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """relevant fields for contact models in product app"""
    email = models.CharField(max_length=254, null=True)
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40, default="anon", null=True)
    inquiry = models.TextField(max_length=250, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
