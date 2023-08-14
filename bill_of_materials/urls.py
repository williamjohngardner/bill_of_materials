from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import logout, login

# import  app.views import *
from app.views import IndexView, CreatePartView, PartListView, PartDetailView, CreateSubAssemblyView, SubAssemblyListView, SubAssemblyDetailView
from app.views import CreateAssemblyView, AssemblyListView, AssemblyDetailView, CreateCustomerView, CustomerListView, CreateSupplierView, SupplierListView
from app.views import CreateProjectView, ProjectListView, ProjectDetailView, CustomerDetailView, SupplierDetailView, CreateSubCategoryView, CreateCategoryView
from app.views import CategoryListView, SubCategoryListView, HighriseView, CreateUserView, ProfilePageView, CreateFinishView, FinishListView, FinishDetailView
from app.views import CreatePlatingView, PlatingListView, PlatingDetailView, AboutView



urlpatterns = [
    path('admin', admin.site.urls),
    # path(r'^', include('django.contrib.auth.paths')),
    path('', IndexView.as_view(), name="index_view"),
    path('highrise/', HighriseView.as_view(), name="highrise_view"),
    path('about', AboutView.as_view(), name="about_view"),
    path('create_user', CreateUserView.as_view(), name="create_user"),
    path('accounts/profile', login_required(ProfilePageView), name="profile_page_view"),
    path('create_category', login_required(CreateCategoryView), name="create_category_view"),
    path('category_list', login_required(CategoryListView), name="category_list_view"),
    path('create_subcategory', login_required(CreateSubCategoryView), name="create_subcategory_view"),
    path('subcategory_list', login_required(SubCategoryListView), name="subcategory_list_view"),
    path('create_part', login_required(CreatePartView), name="create_part_view"),
    path('part_list', login_required(PartListView), name="part_list_view"),
    path('part_list/(?P<pk>\d+)', login_required(PartDetailView), name="part_detail_view"),
    path('create_subassembly', login_required(CreateSubAssemblyView), name="create_subassembly_view"),
    path('subassembly_list', login_required(SubAssemblyListView), name="subassembly_list_view"),
    path('subassembly_list/(?P<pk>\d+)', login_required(SubAssemblyDetailView), name="subassembly_detail_view"),
    path('create_assembly', login_required(CreateAssemblyView), name="create_assembly_view"),
    path('assembly_list', login_required(AssemblyListView), name="assembly_list_view"),
    path('assembly_list/(?P<pk>\d+)', login_required(AssemblyDetailView), name="assembly_detail_view"),
    path('create_customer', login_required(CreateCustomerView), name="create_customer_view"),
    path('customer_list', login_required(CustomerListView), name="customer_list_view"),
    path('customer_list/(?P<pk>\d+)', login_required(CustomerDetailView), name="customer_detail_view"),
    path('create_supplier', login_required(CreateSupplierView), name="create_supplier_view"),
    path('supplier_list', login_required(SupplierListView) , name="supplier_list_view"),
    path('supplier_list/(?P<pk>\d+)', login_required(SupplierDetailView), name="supplier_detail_view"),
    path('create_project', login_required(CreateProjectView), name="create_project_view"),
    path('project_list', login_required(ProjectListView), name="project_list_view"),
    path('project_list/(?P<pk>\d+)', login_required(ProjectDetailView), name="project_detail_view"),
    path('create_finish', login_required(CreateFinishView), name="create_finish_view"),
    path('finish_list', login_required(FinishListView) , name="finish_list_view"),
    path('finish_list/(?P<pk>\d+)', login_required(FinishDetailView), name="finish_detail_view"),
    path('create_plating', login_required(CreatePlatingView), name="create_plating_view"),
    path('plating_list', login_required(PlatingListView) , name="plating_list_view"),
    path('plating_list/(?P<pk>\d+)', login_required(PlatingDetailView), name="plating_detail_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
