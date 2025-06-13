from django.urls import path
from core.dashboard.views import DashboardView, ContactView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    #contact
    path('contact/', ContactView.as_view(), name='contact'),
]