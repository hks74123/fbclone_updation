from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('meramaddatumguddu/', admin.site.urls),
    path('',include('hksfbclone.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})
]
