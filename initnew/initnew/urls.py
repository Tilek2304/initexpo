from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('kafedra_pi/', include('kafedra_pi.urls')),
    path('pi_doc/', include('pi_doc.urls')),
    path('kafedra_ito/', include('kafedra_ito.urls')),
    path('ito_doc/', include('ito_doc.urls')),
    path('ospo_doc/', include('ospo_doc.urls')),
    path('kafedra_ospo/', include('kafedra_ospo.urls')),
    path('od_doc/', include('od_doc.urls')),
    path('kafedra_od/', include('kafedra_od.urls')),
    path('kafedra_init/', include('kafedra_init.urls')),
    path('init_doc/', include('init_doc.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
