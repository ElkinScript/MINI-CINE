from django.views.generic import TemplateView

class DashboardView(TemplateView):
    def get_template_names(self):
        return 'dashboard_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Panel de administración'
        return context