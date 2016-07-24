from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from django.db.models import Sum


from app.models import Part, Assembly, SubAssembly, SubAssemblyQuantity, AssemblyQuantity, Customer, Supplier, Project
from app.forms import CreateSubAssembly


class IndexView(TemplateView):
    template_name = "index.html"


class CreatePartView(CreateView):
    model = Part
    fields = ['part_name', 'part_number', 'description', 'category', 'sub_category', 'manufacturer', 'manufacturer_pn', 'dimensions', 'finish', 'plating', 'uom', 'unit_cost', 'part_url', 'notes', 'cad_file', 'image']
    success_url = reverse_lazy("part_list_view")


class PartListView(ListView):
    model = Part

    def get_queryset(self):
        return Part.objects.all()


class PartDetailView(DetailView):
    model = Part
    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Part.objects.filter(pk=pk)


class SubAssemblyPartInline(InlineFormSet):
    model = SubAssemblyQuantity
    fields = ['part', 'quantity']
    extra = 1


class PartInLine(InlineFormSet):
    model = AssemblyQuantity
    fields = ['part', 'quantity']
    extra = 1


class AssemblyPartInline(InlineFormSet):
    model = AssemblyQuantity
    fields = ['subassembly', 'quantity']
    extra = 1


class CreateSubAssemblyView(CreateWithInlinesView):
    model = SubAssembly
    inlines = [SubAssemblyPartInline]
    fields = ['sub_assembly_name', 'sub_assembly_number', 'description', 'category', 'sub_category', 'mfg_supplier', 'mfg_supplier_pn', 'finish', 'plating', 'notes', 'cad_file']
    success_url = reverse_lazy("subassembly_list_view")


class SubAssemblyListView(ListView):
    model = SubAssembly
    template_name = "app/subassembly_list.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subassembly'] = SubAssembly.objects.all()
        context['unit_cost'] = Part.objects.aggregate(Sum('unit_cost'))
        context['quantity'] = SubAssemblyQuantity.objects.aggregate(Sum('quantity'))
        return context


class SubAssemblyDetailView(DetailView):
    model = SubAssembly

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return SubAssembly.objects.filter(pk=pk)


class SubAssemblyInline(InlineFormSet):
    model = SubAssembly
    fields = ['part', 'quantity']
    extra = 1


class CreateAssemblyView(CreateWithInlinesView):
    model = Assembly
    inlines = [AssemblyPartInline, PartInLine]
    fields = ['assembly_name', 'assembly_part_number', 'description', 'category', 'sub_category', 'supplier', 'supplier_pn', 'finish', 'plating', 'assembly_cost', 'notes', 'cad_file']
    success_url = reverse_lazy("assembly_list_view")


class AssemblyListView(ListView):
    model = Assembly

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assembly'] = Assembly.objects.all()
        return context


class AssemblyDetailView(DetailView):
    model = Assembly

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Assembly.objects.filter(pk=pk)


class CreateCustomerView(CreateView):
    model = Customer
    fields = ['name', 'contact', 'phone', 'email', 'website']
    success_url = reverse_lazy("customer_list_view")


class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Customer.objects.filter(pk=pk)


class CreateSupplierView(CreateView):
    model = Supplier
    fields = ['name', 'contact', 'phone', 'email', 'website']
    success_url = reverse_lazy("supplier_list_view")


class SupplierListView(ListView):
    model = Supplier

    def get_queryset(self):
        return Supplier.objects.all()


class SupplierDetailView(DetailView):
    model = Supplier

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Supplier.objects.filter(pk=pk)


class CreateProjectView(CreateView):
    model = Project
    fields = ['project_number', 'client', 'project_name', 'products', 'quantity_per_product', 'price_per_product', 'extended_price_per_product', 'price_per_project', 'shipping_address', 'shipping_terms', 'expected_delivery']
    success_url = reverse_lazy("project_list_view")


class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Project.objects.filter(pk=pk)
