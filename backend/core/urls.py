from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("idio_main.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.VIDEOS_URL, document_root=settings.VIDEOS_ROOT)