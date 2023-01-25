from django.db import models

# Create your models here.


class Registration(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
