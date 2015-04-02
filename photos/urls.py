#! coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from photos.models import Album, Photo

urlpatterns = patterns('',
  url(r'^$', ListView.as_view(
    model=Album,
    context_object_name='my_album',
    template_name='photo/album.html'),
    name='gallery'
    ),
  url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(
    model=Album,
    context_object_name='photos',
    template_name='photo/photo.html'),
    name='photos'
    ),
)