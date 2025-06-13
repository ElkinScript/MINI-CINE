from django.urls import path, include

from config.urls import urlpatterns

urlpatterns += [
    path('movies/', include('core.movies.urls')),
]