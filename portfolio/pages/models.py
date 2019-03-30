from django.db import models
from PIL import Image


# Create your models here.
class LandingPage(models.Model):
    brand_name = models.CharField(max_length=15)
    brand_name_2 = models.CharField(max_length=15)
    brand_heading = models.TextField(null=True, blank=True)
    brand_paragraph = models.TextField(null=True, blank=True)
    animation_text_1 = models.CharField(max_length=50, null=True, blank=True)
    animation_text_2 = models.CharField(max_length=50, null=True, blank=True)
    animation_text_3 = models.CharField(max_length=20, null=True, blank=True)

    next_page_button = models.CharField(max_length=12)

    facebook_link = models.CharField(max_length=50, default="https://www.facebook.com")
    twitter_link = models.CharField(max_length=50, default="https://www.twitter.com")
    instagram_link = models.CharField(max_length=50, default="https://www.instagram.com")
    github_link = models.CharField(max_length=50, default="https://www.github.com")

    def __str__(self):
        return self.brand_name + ' ' + self.brand_name_2


class AboutPage(models.Model):
    title = models.CharField(max_length=20)
    subheading = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()

    next_page_button = models.CharField(max_length=15)

    image_1 = models.ImageField(upload_to='img/about_images', blank=True)
    image_1_alt = models.CharField(max_length=20, default="Image1")
    image_2 = models.ImageField(upload_to='img/about_images', blank=True)
    image_2_alt = models.CharField(max_length=20, default="Image2")
    image_3 = models.ImageField(upload_to='img/about_images', blank=True)
    image_3_alt = models.CharField(max_length=20, default="Image3")
    image_4 = models.ImageField(upload_to='img/about_images', blank=True)
    image_4_alt = models.CharField(max_length=20, default="Image4")
    image_5 = models.ImageField(upload_to='img/about_images', blank=True)
    image_5_alt = models.CharField(max_length=20, default="Image5")

    def __str__(self):
        return self.title


class ContactPage(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(default="Lorem ipsum Dolor Mita")
    number = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.title