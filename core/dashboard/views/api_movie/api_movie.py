import requests
from django.views.generic import TemplateView

class CurrentMoviesView(TemplateView):
    template_name = "cartelera.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        API_KEY = "bba4a202b6ee1095d6223971aacb8752"
        url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-ES&page=1"

        response = requests.get(url)
        data = response.json()

        context["peliculas"] = data.get("results", [])
        return context
