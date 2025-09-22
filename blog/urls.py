from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from categories.api.router import urlpatterns as categories_router
from post.api.router import urlpatterns as posts_router

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Blog API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router'), name='users-api'),
    path('api/', include(categories_router), name='categories-api'),
    path('api/', include(posts_router), name='posts-api'),
]
