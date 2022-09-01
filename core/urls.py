from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("accounts/", include("allauth.urls")),
    #    path("inventory/", include("inventory.urls")),
    #    path("orders/", include("orders.urls")),
    #    path("sales/", include("sales.urls")),
    path("authentication/", include("authentication.urls", namespace="authentication")),
]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)