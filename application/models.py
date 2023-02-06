from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    dateofbirth = models.DateField()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name