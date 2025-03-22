from django.db import models

# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Contact(models.Model):
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'