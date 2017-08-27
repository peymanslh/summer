# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 13:34
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Used in the URL', max_length=200, verbose_name='Slug')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('last_modified', models.DateField(auto_now=True)),
                ('thumbnail', models.ImageField(default='/Users/peyman/www/python/summer/staticimages/no-img.jpg', upload_to='thumbnails', verbose_name='Thumbnail')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Used in the URL', max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.PostCategory', verbose_name='Category'),
        ),
    ]
