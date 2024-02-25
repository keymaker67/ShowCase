from django.db import models


# Create your models here.
class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active',
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created date',
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated date',
    )

    class Meta:
        abstract = True
        ordering = ('pk', )

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')
