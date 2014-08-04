# -*- coding: utf8 -*-

from django.db import models

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from tinymce.models import HTMLField

from news.util import unique_slugify

class News(models.Model):

    title = models.CharField('Título', max_length=250)
    quick_description = models.CharField('Descrição rápida', max_length=140)
    text = HTMLField(verbose_name='Texto')
    slug = models.SlugField('Link (automático)', blank=True, max_length=250)
    active = models.BooleanField('Ativo', default=True)
    show_on_home = models.BooleanField('Mostrar na home', default=True)
    image = ProcessedImageField(
        blank=True,
        upload_to='news_images/',
        processors=[ResizeToFill(480,362)],
        format='JPEG',
        verbose_name='Imagem',
        options={'quality': 80})
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField('Data')

    def save(self, **kwargs):
        slug_str = self.title
        unique_slugify(self, slug_str)
        super(News, self).save()

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
