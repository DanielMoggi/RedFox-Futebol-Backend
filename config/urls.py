from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router
from RedFox.views import (TimeViewSet,IngressoViewSet,PartidaViewSet,CompraViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()

router.register(r"compras", CompraViewSet)
router.register(r"times", TimeViewSet)
router.register(r"partidas", PartidaViewSet)
router.register(r"ingressos", IngressoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/api", permanent=False)),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)