from rest_framework import serializers
from .models import Company, Contact

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields =  ["id", "name", "country", "revenue"]

class ContactCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "email", "company_id"]

    def to_representation(self, instance):
        self.fields['company_id'] =  CompanySerializer(read_only=True)
        return super(ContactCompanySerializer, self).to_representation(instance)

