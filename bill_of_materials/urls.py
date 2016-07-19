from django.conf.urls import url
from django.contrib import admin

from app.views import IndexView, CreatePartView, PartListView, PartDetailView
from app.views import CreateAssemblyView, AssemblyListView, AssemblyDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_part/$', CreatePartView.as_view(), name="create_part_view"),
    url(r'^part_list/$', PartListView.as_view(), name="part_list_view"),
    url(r'^part_list/(?P<pk>\d+)/$', PartDetailView.as_view(), name="part_detail_view"),
    url(r'^create_assembly/$', CreateAssemblyView.as_view(), name="create_assembly_view"),
    url(r'^assembly_list/$', AssemblyListView.as_view(), name="assembly_list_view"),
    url(r'^assembly_list/(?P<pk>\d+)/$', AssemblyDetailView.as_view(), name="assembly_detail_view")
]
