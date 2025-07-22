from django.contrib.auth.models import AbstractUser
from django.db import models

class customUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('User','User')
    ]
    userTypes = models.CharField(choices = USERTYPE, max_length = 25, null = True)

class portfolioModel(models.Model):
    user = models.OneToOneField(customUserModel, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('ai', 'AI/ML Project'),
        ('design', 'UI/UX Design'),
        ('other', 'Other'),
    ]
    fullName = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()
    thumbnail = models.ImageField(upload_to='static/thumbnails/')
    banner_image = models.ImageField(upload_to='static/banners/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=300)  # e.g., HTML, CSS, JS, Django, SQLite
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    created_at = models.DateTimeField(auto_now_add=True)