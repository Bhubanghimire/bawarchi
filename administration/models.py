from django.db import models


# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo")
    sub_title = models.CharField(max_length=200)
    primary_email = models.EmailField()
    secondary_email = models.EmailField()
    primary_contact = models.CharField(max_length=20)
    secondary_contact = models.CharField(max_length=20)
    openning_hours = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
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
