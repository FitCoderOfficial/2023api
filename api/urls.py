from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi


schema_url_patterns = [ 
    path('accounts/', include('accounts.urls')),
    path('', include('store.api.urls')),
    ]

schema_view = get_schema_view(
    openapi.Info(
        title="2023API",
        default_version='v1',
        description="시스템 API",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)



urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),

    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path("api/", include("store.api.urls")),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
