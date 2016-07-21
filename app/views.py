from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet

from app.models import Part, Assembly, SubAssembly, SubAssemblyQuantity, Customer, Supplier
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
    queryset = Part.objects.all()


class PartInline(InlineFormSet):
    model = SubAssemblyQuantity
    fields = ['part', 'quantity']
    extra = 1


class CreateSubAssemblyView(CreateWithInlinesView):
    model = SubAssembly
    inlines = [PartInline]
    fields = ['sub_assembly_name', 'sub_assembly_number', 'description', 'category', 'sub_category', 'mfg_supplier', 'mfg_supplier_pn', 'finish', 'plating', 'subassembly_cost', 'notes', 'cad_file']
    success_url = reverse_lazy("subassembly_list_view")


class SubAssemblyListView(ListView):
    model = SubAssembly
    template_name = "app/subassemblyquantity_list.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subassembly'] = SubAssembly.objects.all()
        return context


class SubAssemblyDetailView(DetailView):
    pass


class CreateAssemblyView(CreateWithInlinesView):
    model = Assembly
    inlines = [PartInline]
    fields = ['assembly_name', 'assembly_part_number', 'description', 'category', 'sub_category', 'supplier', 'supplier_pn', 'finish', 'plating', 'part_list', 'part_quantity', 'subassembly_list', 'subassembly_quantity', 'assembly_cost', 'notes', 'cad_file']
    success_url = reverse_lazy("assembly_list_view")



class AssemblyListView(ListView):
    model = Assembly

    def get_queryset(self):
        return Assembly.objects.all()


class AssemblyDetailView(DetailView):
    pass


class CreateCustomerView(CreateView):
    model = Customer
    fields = ['name', 'contact', 'phone', 'email', 'website']
    success_url = reverse_lazy("customer_list_view")


class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        return Customer.objects.all()


class CreateSupplierView(CreateView):
    model = Supplier
    fields = ['name', 'contact', 'phone', 'email', 'website']
    success_url = reverse_lazy("supplier_list_view")


class SupplierListView(ListView):
    model = Supplier

    def get_queryset(self):
        return Supplier.objects.all()
