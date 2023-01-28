from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    amount = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('phone',)
    def __str__(self):
        return self.phone
