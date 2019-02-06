# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from rest_framework import generics

from .models import Company, Contact
from .serializers import CompanySerializer, ContactCompanySerializer

class RESTContactDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactCompanySerializer


class RESTContactListByCompany(generics.ListAPIView):

    def get_serializer_class(self):
        if self.request.GET.get('revenue_gte'):
            return CompanySerializer
        elif self.request.GET.get('name'):
            return ContactCompanySerializer
        else:
            return ContactCompanySerializer

    def get_queryset(self):
        """ 
        This view should return a list of all the contacts by
        filtering against 'company_id', 'revenue', 'name' query 
        parameters in the url.
        """

        company_id = self.request.GET.get('company_id', None)
        revenue_gte = self.request.GET.get('revenue_gte', None)
        name = self.request.GET.get('name', None)

        if company_id is not None:
            return Contact.objects.filter(company_id=company_id)
        elif name is not None:
            return Contact.objects.filter(name=name)
        elif revenue_gte is not None:
            return Company.objects.filter(revenue__gte=revenue_gte)
        return Contact.objects.all()
\