from django.conf.urls import url
from django.contrib import admin

from app.views import IndexView, CreatePartView, PartListView, PartDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_part/$', CreatePartView.as_view(), name="create_part_view"),
    url(r'^part_list/$', PartListView.as_view(), name="part_list_view"),
    url(r'^part_list/(?P<pk>\d+)/$', PartDetailView.as_view(), name="part_detail_view")
]
