# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import \
     python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Company(models.Model):
    id= models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(_('name'), max_length=50)
    country = models.CharField(_('country'), max_length=50)
    revenue = models.PositiveIntegerField(_('revenue'))

    def __str__(self):
        return self.name    
        
    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

@python_2_unicode_compatible
class Contact(models.Model):
    id = models.PositiveIntegerField(_('contact_id'), primary_key=True, unique=True)
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'))
    company_id = models.ForeignKey(Company, related_name='company_id')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

