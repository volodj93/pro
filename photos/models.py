#! coding: utf-8
from django.db import models
#Альбом с фотографиями
class Album(models.Model):
    title = models.CharField("Название альбома", max_length=100)
    slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
    img = models.ImageField("Изображение альбома", upload_to='images',
	help_text='Размер изображения 200px на 200px')
    class Meta:
        ordering = ['title']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
    def __unicode__(self):
        return self.title
#Фотографии в альбоме
class Photo(models.Model):
    title = models.CharField("Название фотографии", max_length=100)
    album = models.ForeignKey(Album, verbose_name='Альбом')
    img = models.ImageField("Фото", upload_to='images',
	help_text='Желательно, чтоб фото было не большого размера')
    class Meta:
        ordering = ['title']
        verbose_name = 'Фото'
        verbose_name_plural = "Фотографии"
    def __unicode__(self):
        return self.title