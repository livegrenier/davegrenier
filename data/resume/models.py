from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django import forms


class photo(models.Model):
    file = models.FileField(default='', upload_to='site_media')

class about(models.Model):
    title = models.CharField(default='', max_length=200)
    content = RichTextField(default='')
    subtitle = models.CharField(default='', max_length=200)
    pdf = models.FileField(default='', upload_to='site_media') 
    pdf_icon = models.FileField(default='', upload_to='site_media') 
    def __str__(self):
        return self.title

class intro(models.Model):
    title = models.CharField(default='', max_length=200)
    text = models.TextField(default='')
    content = RichTextField(default='')
    email = models.CharField(default='', max_length=200)
    def __str__(self):
        return self.title

class experiance(models.Model):
    class Meta:
        ordering = ['number_list']
    number_list = models.CharField(default='#', max_length=11)
    title = models.CharField(default='', max_length=200)
    sub_title = models.CharField(default='', max_length=200)
    job_title = models.CharField(default='', max_length=200)
    content = RichTextField(default='')
    start_date = models.CharField(default="2000-12-31", max_length=11)
    end_date = models.CharField(default='Present', max_length=11)
    def __str__(self):
        return self.title

class skill(models.Model):
    title = models.CharField(default='', max_length=200)
    content = RichTextField(default='')
    def __str__(self):
        return self.title

class skill_icon(models.Model):
    file = models.FileField(default='', upload_to='site_media') 