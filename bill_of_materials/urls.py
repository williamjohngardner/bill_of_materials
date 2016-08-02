from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login


from app.views import IndexView, CreatePartView, PartListView, PartDetailView, CreateSubAssemblyView, SubAssemblyListView, SubAssemblyDetailView
from app.views import CreateAssemblyView, AssemblyListView, AssemblyDetailView, CreateCustomerView, CustomerListView, CreateSupplierView, SupplierListView
from app.views import CreateProjectView, ProjectListView, ProjectDetailView, CustomerDetailView, SupplierDetailView, CreateSubCategoryView, CreateCategoryView
from app.views import CategoryListView, SubCategoryListView, HighriseView, CreateUserView, ProfilePageView, CreateFinishView, FinishListView, FinishDetailView, CreatePlatingView, PlatingListView, PlatingDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^highrise/$', HighriseView.as_view(), name="highrise_view"),
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user"),
    url(r'^accounts/profile/$', login_required(ProfilePageView.as_view()), name="profile_page_view"),
    url(r'^create_category/$', login_required(CreateCategoryView.as_view()), name="create_category_view"),
    url(r'^category_list/$', login_required(CategoryListView.as_view()), name="category_list_view"),
    url(r'^create_subcategory/$', login_required(CreateSubCategoryView.as_view()), name="create_subcategory_view"),
    url(r'^subcategory_list/$', login_required(SubCategoryListView.as_view()), name="subcategory_list_view"),
    url(r'^create_part/$', login_required(CreatePartView.as_view()), name="create_part_view"),
    url(r'^part_list/$', login_required(PartListView.as_view()), name="part_list_view"),
    url(r'^part_list/(?P<pk>\d+)/$', login_required(PartDetailView.as_view()), name="part_detail_view"),
    url(r'^create_subassembly/$', login_required(CreateSubAssemblyView.as_view()), name="create_subassembly_view"),
    url(r'^subassembly_list/$', login_required(SubAssemblyListView.as_view()), name="subassembly_list_view"),
    url(r'^subassembly_list/(?P<pk>\d+)/$', login_required(SubAssemblyDetailView.as_view()), name="subassembly_detail_view"),
    url(r'^create_assembly/$', login_required(CreateAssemblyView.as_view()), name="create_assembly_view"),
    url(r'^assembly_list/$', login_required(AssemblyListView.as_view()), name="assembly_list_view"),
    url(r'^assembly_list/(?P<pk>\d+)/$', login_required(AssemblyDetailView.as_view()), name="assembly_detail_view"),
    url(r'^create_customer/$', login_required(CreateCustomerView.as_view()), name="create_customer_view"),
    url(r'^customer_list/$', login_required(CustomerListView.as_view()), name="customer_list_view"),
    url(r'^customer_list/(?P<pk>\d+)/$', login_required(CustomerDetailView.as_view()), name="customer_detail_view"),
    url(r'^create_supplier/$', login_required(CreateSupplierView.as_view()), name="create_supplier_view"),
    url(r'^supplier_list/$', login_required(SupplierListView.as_view()) , name="supplier_list_view"),
    url(r'^supplier_list/(?P<pk>\d+)/$', login_required(SupplierDetailView.as_view()), name="supplier_detail_view"),
    url(r'^create_project/$', login_required(CreateProjectView.as_view()), name="create_project_view"),
    url(r'^project_list/$', login_required(ProjectListView.as_view()), name="project_list_view"),
    url(r'^project_list/(?P<pk>\d+)/$', login_required(ProjectDetailView.as_view()), name="project_detail_view"),
    url(r'^create_finish/$', login_required(CreateFinishView.as_view()), name="create_finish_view"),
    url(r'^finish_list/$', login_required(FinishListView.as_view()) , name="finish_list_view"),
    url(r'^finish_list/(?P<pk>\d+)/$', login_required(FinishDetailView.as_view()), name="finish_detail_view"),
    url(r'^create_plating/$', login_required(CreatePlatingView.as_view()), name="create_plating_view"),
    url(r'^plating_list/$', login_required(PlatingListView.as_view()) , name="plating_list_view"),
    url(r'^plating_list/(?P<pk>\d+)/$', login_required(PlatingDetailView.as_view()), name="plating_detail_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
