from django.urls import path, include  # add this
from rest_framework.routers import DefaultRouter  # add this
from .views import (
    ContactList,
    new_contact, contact_details,
    update_contact, delete_contact
)
from .api import ContactViewSet  # add this
router = DefaultRouter()  # add this
router.register(r'contacts', ContactViewSet,
                basename='contact')  # add this


urlpatterns = [
    path("api/", include(router.urls)),
    path("contacts/", ContactList.as_view(), name="contacts"),
    path("contacts/new/", new_contact, name="new"),
    path("contacts/<int:id>/details/", contact_details, name="details"),
    path("contacts/<int:id>/update/", update_contact, name="update"),
    path("contacts/<int:id>/delete/", delete_contact, name="delete"),
]
