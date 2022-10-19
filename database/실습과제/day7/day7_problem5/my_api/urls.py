from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      # 프로젝트 이름
      title="SSAFY DJANGO 프로젝트",
      # 프로젝트 버전
      default_version='v1',
      # 해당 문서 설명
      description="DJANGO 실습 프로젝트 입니다.",
      # SERVICE 기한
      terms_of_service="https://www.google.com/policies/terms/",
      # 부가 정보
      contact=openapi.Contact(email="내 이메일"),
      # 부가 정보
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]