from django.db import models

# Create your models here.
class UserAccount(models.Model):
    user_name = models.CharField(max_length=40)
    user_password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name+self.user_password