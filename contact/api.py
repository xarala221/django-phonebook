# contact/api.py
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
