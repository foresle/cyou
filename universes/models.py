from django.db import models
from django.contrib.auth import get_user_model


class Universe(models.Model):
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=80, null=False, blank=False, default='My Own Universe')
    description = models.CharField(max_length=800, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    universe = models.ForeignKey(to=Universe, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=120, null=False, blank=False, default='A New Post')
    payload = models.CharField(max_length=6000, null=False, blank=False)

    def __str__(self):
        return self.name
