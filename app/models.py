from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=20)

    def __str__(self):
        return self.subcategory


class ShippingTerms(models.Model):
    shipping_type = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    preferred_shipper = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.shipping_type


class Part(models.Model):
    part_name = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    manufacturer = models.ForeignKey('app.Supplier', null=True, blank=True)
    manufacturer_pn = models.CharField(max_length=50, null=True, blank=True)
    dimensions = models.CharField(max_length=30)
    finish = models.ForeignKey('app.FinishTable', null=True, blank=True)
    plating = models.ForeignKey('app.PlatingTable', null=True, blank=True)
    uom = models.CharField(max_length=15)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    part_url = models.URLField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    cad_file = models.FileField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # many of these fields need to be Null=True

    def __str__(self):
        return self.part_name


class SubAssembly(models.Model):
    sub_assembly_name = models.CharField(max_length=50)
    sub_assembly_number = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    manufacturer = models.ForeignKey('app.Supplier', null=True, blank=True)
    manufacturer_pn = models.CharField(max_length=50, null=True, blank=True)
    dimensions = models.CharField(max_length=30)
    finish = models.ForeignKey('app.FinishTable', null=True, blank=True)
    plating = models.ForeignKey('app.PlatingTable', null=True, blank=True)
    uom = models.CharField(max_length=15)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    part_url = models.URLField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    cad_file = models.FileField(null=True, blank=True)
    # many of these fields need to be Null=True

    def __str__(self):
        return self.sub_assembly_name


class Assembly(models.Model):
    assembly_name = models.CharField(max_length=50)
    assembly_part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    supplier = models.ForeignKey('app.Supplier', null=True, blank=True)
    supplier_pn = models.CharField(max_length=50, null=True, blank=True)
    list_of_parts = models.ManyToManyField(Part, null=True, blank=True)
    list_of_assemblies = models.ForeignKey(SubAssembly, null=True, blank=True)
    quantity = models.IntegerField()
    extended_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()
    cad_file = models.FileField()
    # many of these fields need to be Null=True

    def __str__(self):
        return self.assembly_name


class Project(models.Model):
    project_number = models.AutoField(primary_key=True)
    client = models.ForeignKey('app.Customer')
    product = models.ManyToManyField(Assembly)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_address = models.TextField()
    shipping_terms = models.ForeignKey(ShippingTerms, null=True, blank=True)
    expected_delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.product


class Customer(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    orders = models.ManyToManyField(Project, null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    items_supplied = models.ManyToManyField(Part, null=True, blank=True)

    def __str__(self):
        return self.name


class FinishTable(models.Model):
    finish = models.CharField(max_length=20)
    description = models.TextField()
    source = models.ForeignKey(Supplier, null=True, blank=True)

    def __str__(self):
        return self.finish


class PlatingTable(models.Model):
    plating = models.CharField(max_length=20)
    description = models.TextField()
    source = models.ForeignKey(Supplier, null=True, blank=True)

    def __str__(self):
        return self.plating
