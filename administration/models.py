from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from system.models import ConfigChoice


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo")
    sub_title = models.CharField(max_length=200)
    openning_hour = models.CharField(max_length=200)
    description = models.TextField()
    primary_email = models.EmailField()
    secondary_email = models.EmailField()
    primary_contact = models.CharField(max_length=20)
    secondary_contact = models.CharField(max_length=20)
    openning_hours = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    instagram = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ABOUT"


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "CONTACT US"


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "GALLERY"


class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ConfigChoice, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    image = models.ImageField(upload_to="item")
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ITEMS'


class OpeningHours(models.Model):
    DAY_CHOICE = (
        ("Sunday", "Sunday"),
        ("Tuesday", "Tuesday"),
        ("Thursday", "Thursday"),
        ("Saturday", "Saturday")
    )
    day = models.CharField(max_length=100, choices=DAY_CHOICE)
    time = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.day

    class Meta:
        unique_together = ('day', 'time')
        verbose_name_plural = 'OPENNING HOUR'


class Staff(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="staff")
    position = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.URLField()
    instagram = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'STAFF'


class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=20)
    image = models.ImageField(upload_to="testimonial")
    comment = models.TextField()
    rating = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'TESTIMONIALS'


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'SUBSCRIBER'
