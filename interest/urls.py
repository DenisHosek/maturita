from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("interest.interests.urls")),
    path("admin/", admin.site.urls, name="admin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
