from django.views.generic import ListView

from universes.models import Universe


class DashboardView(ListView):
    template_name = 'dashboard/dashboard.html'
    model = Universe
