# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0')),
                ('img', models.ImageField(help_text=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f 200px \xd0\xbd\xd0\xb0 200px', upload_to=b'images', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd1\x84\xd0\xb8\xd0\xb8')),
                ('img', models.ImageField(help_text=b'\xd0\x96\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe, \xd1\x87\xd1\x82\xd0\xbe\xd0\xb1 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe \xd0\xb1\xd1\x8b\xd0\xbb\xd0\xbe \xd0\xbd\xd0\xb5 \xd0\xb1\xd0\xbe\xd0\xbb\xd1\x8c\xd1\x88\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb0', upload_to=b'images', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe')),
                ('album', models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc', to='photos.Album')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0424\u043e\u0442\u043e',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
            bases=(models.Model,),
        ),
    ]
