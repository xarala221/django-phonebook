from django.urls import path
from .views import (index, contact_list, new_contact, contact_details,
                    update_contact, delete_contact)

urlpatterns = [
    path("", index, name="home"),
    path("contacts/", contact_list, name="contacts"),
    path("contacts/new/", new_contact, name="new"),
    path("contacts/<int:id>/details/", contact_details, name="details"),
    path("contacts/<int:id>/update/", update_contact, name="update"),
    path("contacts/<int:id>/delete/", delete_contact, name="delete"),
]
