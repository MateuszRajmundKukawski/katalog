from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from parts.views import PartListView, PartDetailView

urlpatterns =  patterns(
    '',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^lista_czesci/$', PartListView.as_view(), name='part-listview'),
    url(r'^$', PartListView.as_view()),
    url(r'^lista_czesci/(?P<pk>\d+)/$', PartDetailView.as_view(), name='part-detailview'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
