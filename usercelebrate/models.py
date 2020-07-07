from django.db import models
from userlist.models import Children
from datetime import datetime

class Celebrate(models.Model):
    children = models.ForeignKey(Children, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now())
    visit = models.IntegerField(
        max_length=1,
        choices=(
            (0, "Ушел"),
            (1, "Пришел")
        )
    )