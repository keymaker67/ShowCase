from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)
from .local_settings import ADMIN_PATH

urlpatterns = [
    path(f'{ADMIN_PATH}/', admin.site.urls),
    path('', include('content.urls')),
    path('user/', include('user.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)
