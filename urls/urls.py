from django.urls import include, path

urlpatterns = [
    path('v1/', include('urls.versions.v1', namespace='v1')),
]
