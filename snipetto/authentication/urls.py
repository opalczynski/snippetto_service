from django.urls import path

from snipetto.authentication.views import InitializeUserView

urlpatterns = [
    path('init/', InitializeUserView.as_view(), name='user-init')
]
