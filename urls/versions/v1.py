from django.urls import include, path

app_name = 'app'

urlpatterns = [
    path('snippets/', include('snipetto.snippets.urls')),
]
