from django.urls import path

from snipetto.core.views import UrlsMappingAPIView

urlpatterns = [
    path('paths/', UrlsMappingAPIView.as_view(), name='api-paths')
]
