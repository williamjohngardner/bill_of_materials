from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet
from django.db.models import Sum
from highton import Highton
import os


from app.models import Part, Assembly, SubAssembly, SubAssemblyQuantity, AssemblyQuantity, Customer, Supplier, Project, ProjectQuantity, Category, SubCategory
from app.forms import CreateCustomer, CreateSupplier


class IndexView(TemplateView):
    template_name = "index.html"


class HighriseView(TemplateView):
    template_name = "highrise.html"


class CreateCategoryView(CreateView):
    model = Category
    fields = ['category']
    success_url = reverse_lazy("category_list_view")


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()


class CreateSubCategoryView(CreateView):
    model = SubCategory
    fields = ['category', 'subcategory']
    success_url = reverse_lazy("subcategory_list_view")


class SubCategoryListView(ListView):
    model = SubCategory

    def get_queryset(self):
        return SubCategory.objects.all()


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
    fields = ['part', 'subassembly', 'quantity']
    extra = 1


class ProjectPartInline(InlineFormSet):
    model = ProjectQuantity
    fields = ['assembly', 'quantity', 'price_per_assembly']
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
    inlines = [AssemblyPartInline]
    fields = ['assembly_name', 'assembly_part_number', 'description', 'category', 'sub_category', 'supplier', 'supplier_pn', 'finish', 'plating', 'assembly_cost', 'notes', 'cad_file']
    success_url = reverse_lazy("assembly_list_view")


class AssemblyListView(ListView):
    model = Assembly

    def get_queryset(self):
        return self.model.objects.all()


class AssemblyDetailView(DetailView):
    model = Assembly

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Assembly.objects.filter(pk=pk)


class CreateProjectView(CreateWithInlinesView):
    model = Project
    inlines = [ProjectPartInline]
    fields = ['project_number', 'client', 'project_name', 'price_per_project', 'shipping_address', 'shipping_terms', 'expected_delivery']
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


class CreateCustomerView(CreateView):
    model = Customer
    form_class = CreateCustomer
    # fields = ['name', 'contact', 'phone', 'email', 'website']
    success_url = reverse_lazy("customer_list_view")

    def form_valid(self, form):
        high = Highton(
            api_key = os.environ['highrise_api_key'],
            user = 'williamjohngardner')
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        title = form.cleaned_data["title"]
        company_name = form.cleaned_data["company_name"]
        phone_number = form.cleaned_data["phone_number"]
        email_address = form.cleaned_data["email_address"]
        twitter_account = form.cleaned_data["twitter_account"]
        web_address = form.cleaned_data["web_address"]
        street_address = form.cleaned_data["street_address"]
        city = form.cleaned_data["city"]
        state = form.cleaned_data["state"]
        zip_code = form.cleaned_data["zip_code"]
        country = form.cleaned_data["country"]

        customer = "<person><first-name>{}</first-name><last-name>{}</last-name><title>{}</title><company-name>{}</company-name><contact-data><email-addresses><email-address><address></address></email-address></email-addresses><phone-numbers><phone-number><id>4433405272</id><number>{}</number></phone-number></phone-numbers><twitter-accounts><twitter-account><username>{}</username><url>http://twitter.com/{}</url></twitter-account></twitter-accounts><web-addresses><web-address><id>214243865</id><url>{}</url></web-address></web-addresses><addresses><address><street>{}</street><city>{}</city><state>{}</state><zip>{}</zip><id>129411272</id><country>{}</country></address></addresses></contact-data></person>".format(first_name, last_name, title, company_name, phone_number, email_address, twitter_account, twitter_account, web_address, street_address, city, state, zip_code, country)
        high.post_person(customer)
        return super().form_valid(form)


class CustomerListView(ListView):
    model = Customer

    def get_queryset(self):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        high = Highton(
            api_key = os.environ['highrise_api_key'],
            user = 'williamjohngardner')
        context["people"] = high.get_people()
        for person in context['people']:
            Customer.objects.update_or_create(first_name=person.first_name, last_name=person.last_name, title=person.title, company_name=person.company_name, email_address=person.email_addresses)

        return context


class CustomerDetailView(DetailView):
    model = Customer

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Customer.objects.filter(pk=pk)


class CreateSupplierView(CreateView):
    model = Supplier
    form_class = CreateSupplier
    # fields = ['name', 'contact', 'phone', 'email', 'website']
    success_url = reverse_lazy("supplier_list_view")

    def form_valid(self, form):
        high = Highton(
            api_key = os.environ['highrise_api_key'],
            user = 'williamjohngardner')
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        title = form.cleaned_data["title"]
        company_name = form.cleaned_data["company_name"]
        phone_number = form.cleaned_data["phone_number"]
        email_address = form.cleaned_data["email_address"]
        twitter_account = form.cleaned_data["twitter_account"]
        web_address = form.cleaned_data["web_address"]
        street_address = form.cleaned_data["street_address"]
        city = form.cleaned_data["city"]
        state = form.cleaned_data["state"]
        zip_code = form.cleaned_data["zip_code"]
        country = form.cleaned_data["country"]


        supplier = "<person><first-name>{}</first-name><last-name>{}</last-name><title>{}</title><company-name>{}</company-name><contact-data><email-addresses><email-address><address>{}</address></email-address></email-addresses><phone-numbers><phone-number><id>4433405272</id><number>{}</number></phone-number></phone-numbers><twitter-accounts><twitter-account><username>{}</username><url>http://twitter.com/{}</url></twitter-account></twitter-accounts><web-addresses><web-address><id>214243865</id><url>{}</url></web-address></web-addresses><addresses><address><street>{}</street><city>{}</city><state>{}</state><zip>{}</zip><id>129411272</id><country>{}</country></address></addresses></contact-data></person>".format(first_name, last_name, title, company_name, phone_number, email_address, twitter_account, twitter_account, web_address, street_address, city, state, zip_code, country)
        high.post_person(supplier)
        return super().form_valid(form)


class SupplierListView(ListView):
    model = Supplier

    def get_queryset(self):
        return Supplier.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        high = Highton(
            api_key = os.environ['highrise_api_key'],
            user = 'williamjohngardner')
        context["people"] = high.get_people()
        for person in context['people']:
            Supplier.objects.update_or_create(first_name=person.first_name, last_name=person.last_name, title=person.title, company_name=person.company_name)

        return context


class SupplierDetailView(DetailView):
    model = Supplier

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        return Supplier.objects.filter(pk=pk)
