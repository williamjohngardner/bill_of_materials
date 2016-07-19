from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from app.models import Part, Assembly


class IndexView(TemplateView):
    template_name = "index.html"


class CreatePartView(CreateView):
    model = Part
    fields = ['part_name', 'part_number', 'description', 'category', 'sub_category', 'manufacturer', 'manufacturer_pn', 'dimensions', 'finish', 'plating', 'uom', 'cost_per_unit', 'part_url', 'notes', 'cad_file', 'image']
    success_url = reverse_lazy("part_list_view")


class PartListView(ListView):
    model = Part

    def get_queryset(self):
        return Part.objects.all()


class PartDetailView(DetailView):
    model = Part
    queryset = Part.objects.all()


class CreateAssemblyView(CreateView):
    model = Assembly
    fields = ['assembly_name', 'assembly_part_number', 'description', 'category', 'sub_category', 'supplier', 'supplier_pn', 'list_of_parts', 'list_of_assemblies', 'quantity', 'extended_price', 'notes', 'cad_file']
    success_url = reverse_lazy("assembly_list_view")


class AssemblyListView(ListView):
    model = Assembly

    def get_queryset(self):
        return Assembly.objects.all()


class AssemblyDetailView(DetailView):
    pass
