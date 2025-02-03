from django.contrib import admin
from django.urls import path, include
from .local_settings import ADMIN_URL
from .views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path(f'{ADMIN_URL}/', admin.site.urls),
    path('', home, name='home'),
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls'))  # For login, logout, and registration
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
