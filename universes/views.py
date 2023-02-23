from django.db.models import Prefetch
from django.views.generic import DetailView

from .models import Universe, Post


class UniverseDetailView(DetailView):
    model = Universe
    queryset = Universe.objects.prefetch_related('post_set')
