from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_Length=200)
    completed = models.BooleanField(default=False)
