from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [

    # ================= DJANGO ADMIN =================

    path(
        'django-admin/',
        admin.site.urls
    ),

    # ================= APP URLS =================

    path(
        '',
        include('books.urls')
    ),

]


# ================= MEDIA FILES =================

if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT

    )