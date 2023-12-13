from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_COISE = [['Pending', 'Pending'], ['Completed', 'Completed']]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_COISE)

    def __str__(self) -> str:
        return self.title
