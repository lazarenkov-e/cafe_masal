from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.lastname} {self.name}'
