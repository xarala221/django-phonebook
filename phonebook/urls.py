from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("contact.urls")),  # add this
    path("", include("accounts.urls")),  # add this
    path("", include("pages.urls"))  # new
]
