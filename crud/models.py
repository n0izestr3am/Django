# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)

class Anggota(models.Model):
    nama = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    departement = models.CharField(max_length=255, blank=True)
    pekerjaan = models.CharField(max_length=255, blank=True)
    telp = models.CharField(max_length=255, blank=True)
    kota = models.CharField(max_length=255, blank=True)
    aktif_keanggotaan = models.CharField(max_length=255, blank=True)
    jabatan = models.CharField(max_length=255, blank=True)
    alamat = models.TextField(max_length=255, blank=True)
    foto = models.CharField(max_length=254 ,blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
