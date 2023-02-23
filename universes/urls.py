from django.urls import path

from .views import UniverseDetailView

app_name = 'universes'

urlpatterns = [
    path('<int:pk>/', UniverseDetailView.as_view(), name='detail'),
]
