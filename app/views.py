from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from app.models import Part


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
