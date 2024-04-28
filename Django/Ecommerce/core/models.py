from django.db import models


class MyBaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")

    class Meta:
        abstract = True
        ordering = ('pk', )

    def __str__(self):
        raise NotImplementedError("Implement __str__ method")
