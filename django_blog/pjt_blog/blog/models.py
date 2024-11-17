from django.db import models

# Create your models here.
class PostModel(models.Model):
    id=models.BigAutoField(
        primary_key=True
    )
    title=models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name='title'

    )

    content=models.TextField(
        max_length=30,
        verbose_name='descrption'
    )
    pdate=models.DateField()
    author=models.CharField(
        max_length=50,
    )