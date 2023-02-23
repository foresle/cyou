from django.contrib import admin
from django.urls import path, include

# Customization admin site titles
admin.site.site_header = 'cyou admin'
admin.site.site_title = 'cyou admin site'
admin.site.index_title = 'cyou admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('universes/', include('universes.urls', namespace='universes')),
    path('', include('dashboard.urls'))
]
