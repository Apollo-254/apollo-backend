from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/v1/', include('auth_apps.urls'), name="auth"),

    # documentation urls
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-schema'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handling error 404 and 500 (the error view is configured under utils folder)
handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'
