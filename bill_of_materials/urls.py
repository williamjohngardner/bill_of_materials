from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from app.views import IndexView, CreatePartView, PartListView, PartDetailView, CreateSubAssemblyView, SubAssemblyListView, SubAssemblyDetailView
from app.views import CreateAssemblyView, AssemblyListView, AssemblyDetailView, CreateCustomerView, CustomerListView, CreateSupplierView, SupplierListView
from app.views import CreateProjectView, ProjectListView, ProjectDetailView, CustomerDetailView, SupplierDetailView, CreateSubCategoryView, CreateCategoryView
from app.views import CategoryListView, SubCategoryListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_category/$', CreateCategoryView.as_view(), name="create_category_view"),
    url(r'^category_list/$', CategoryListView.as_view(), name="category_list_view"),
    url(r'^create_subcategory/$', CreateSubCategoryView.as_view(), name="create_subcategory_view"),
    url(r'^subcategory_list/$', SubCategoryListView.as_view(), name="subcategory_list_view"),
    url(r'^create_part/$', CreatePartView.as_view(), name="create_part_view"),
    url(r'^part_list/$', PartListView.as_view(), name="part_list_view"),
    url(r'^part_list/(?P<pk>\d+)/$', PartDetailView.as_view(), name="part_detail_view"),
    url(r'^create_subassembly/$', CreateSubAssemblyView.as_view(), name="create_subassembly_view"),
    url(r'^subassembly_list/$', SubAssemblyListView.as_view(), name="subassembly_list_view"),
    url(r'^subassembly_list/(?P<pk>\d+)/$', SubAssemblyDetailView.as_view(), name="subassembly_detail_view"),
    url(r'^create_assembly/$', CreateAssemblyView.as_view(), name="create_assembly_view"),
    url(r'^assembly_list/$', AssemblyListView.as_view(), name="assembly_list_view"),
    url(r'^assembly_list/(?P<pk>\d+)/$', AssemblyDetailView.as_view(), name="assembly_detail_view"),
    url(r'^create_customer/$', CreateCustomerView.as_view(), name="create_customer_view"),
    url(r'^customer_list/$', CustomerListView.as_view(), name="customer_list_view"),
    url(r'^customer_list/(?P<pk>\d+)/$', CustomerDetailView.as_view(), name="customer_detail_view"),
    url(r'^create_supplier/$', CreateSupplierView.as_view(), name="create_supplier_view"),
    url(r'^supplier_list/$', SupplierListView.as_view(), name="supplier_list_view"),
    url(r'^supplier_list/(?P<pk>\d+)/$', SupplierDetailView.as_view(), name="supplier_detail_view"),
    url(r'^create_project/$', CreateProjectView.as_view(), name="create_project_view"),
    url(r'^project_list/$', ProjectListView.as_view(), name="project_list_view"),
    url(r'^project_list/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name="project_detail_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
