from django.db import models
from django.db.models.fields import CharField, SlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
