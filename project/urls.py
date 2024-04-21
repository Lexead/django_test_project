from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(
        "api/",
        include(
            [
                path(
                    "v1/",
                    include(
                        [
                            path("auth/", include("djoser.urls")),
                            path("auth/", include("djoser.urls.jwt")),
                            path("links/", include("links.urls")),
                        ]
                    ),
                )
            ]
        ),
    ),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema-swagger-json"), name="schema-swagger-ui"),
    path("swagger.yaml/", SpectacularAPIView.as_view(), name="schema-swagger-yaml"),
    path("swagger.json/", SpectacularJSONAPIView.as_view(), name="schema-swagger-json"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema-swagger-yaml"), name="schema-redoc"),
]
