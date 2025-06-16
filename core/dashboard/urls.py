from django.urls import path
from core.dashboard.views import DashboardView, ContactView
from core.dashboard.views.api_movie import CurrentMoviesView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    #contact
    path('contact/', ContactView.as_view(), name='contact'),

    # API Movie
    path('api-movie/', CurrentMoviesView.as_view(), name='api_movie'),
]