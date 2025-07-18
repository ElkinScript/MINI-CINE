from django.views.generic import TemplateView
from django.conf import settings
import requests

class UpcomingReleasesView(TemplateView):
    template_name = "proximos-estrenos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_key = settings.TMDB_API_KEY
        url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=es-ES&page=1"
        response = requests.get(url)
        data = response.json()
        context['peliculas'] = data.get('results', [])
        return context