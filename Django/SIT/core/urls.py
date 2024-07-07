from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .local_settings import ADMIN_PATH
urlpatterns = [
    path(f'{ADMIN_PATH}/', admin.site.urls),
    path('', include('home.urls', 'home'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)
