from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from app.models import Part, Assembly, SubAssembly, Quantity, Customer, Supplier
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


class CreateSubAssemblyView(CreateView):
    model = SubAssembly
    form = CreateSubAssembly
    fields = ['sub_assembly_name', 'sub_assembly_number', 'description', 'category', 'sub_category', 'mfg_supplier', 'mfg_supplier_pn', 'finish', 'plating', 'part_list', 'subassembly_list', 'subassembly_quantity', 'subassembly_cost', 'notes', 'cad_file']
    # model = Quantity
    # fields = ['part', 'quantity', 'assembly']
    success_url = reverse_lazy("subassembly_list_view")


class SubAssemblyListView(ListView):
    model = SubAssembly

    def get_queryset(self):
        return SubAssembly.objects.all()


class SubAssemblyDetailView(DetailView):
    pass


class CreateAssemblyView(CreateView):
    model = Assembly
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
