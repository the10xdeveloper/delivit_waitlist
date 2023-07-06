from django.db import models


# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=255, verbose_name="What\'s your name?")
    email = models.CharField(max_length=255, verbose_name="What\'s your email address?")

    def __str__(self):
        return self.email

    pass


class UserDetail(models.Model):
    user = models.OneToOneField(to=UserData, on_delete=models.PROTECT)
    phone = models.CharField(max_length=11, verbose_name="What\'s your phone number?")
    state = models.CharField(max_length=255, verbose_name="What\'s your state of residence?")

    def __str__(self):
        return self.user.email
