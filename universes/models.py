from django.db import models
from django.contrib.auth import get_user_model


class Universe(models.Model):
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=80, null=False, blank=False, default='My Own Universe')
    description = models.CharField(max_length=800, null=False, blank=False)

    def __str__(self):
        return self.name
