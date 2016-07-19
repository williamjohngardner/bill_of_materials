from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=30)

    def __str__(self):
        return self.subcategory


class ShippingTerms(models.Model):
    shipping_type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    preferred_shipper = models.CharField(max_length=50, null=True, blank=True)

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
    dimensions = models.CharField(max_length=50)
    finish = models.ForeignKey('app.FinishTable', null=True, blank=True)
    plating = models.ForeignKey('app.PlatingTable', null=True, blank=True)
    uom = models.CharField(max_length=15)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
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
    description = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True)
    mfg_supplier = models.ForeignKey('app.Supplier', null=True, blank=True)
    mfg_supplier_pn = models.CharField(max_length=50, null=True, blank=True)
    finish = models.ForeignKey('app.FinishTable', null=True, blank=True)
    plating = models.ForeignKey('app.PlatingTable', null=True, blank=True)
    part_list = models.ManyToManyField(Part)
    part_quantity = models.IntegerField(null=True, blank=True)
    subassembly_list = models.ManyToManyField('app.SubAssembly')
    subassembly_quantity = models.IntegerField(null=True, blank=True)
    subassembly_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    cad_file = models.FileField(null=True, blank=True)
    # many of these fields need to be Null=True

    def subassembly_cost(self):
        parts_cost = self.part_list.aggregate(total=models.Sum('unit_cost'))['total']
        subassembly_cost = self.subassembly_list.aggregate(total=models.Sum('unit_cost'))['total']
        total_cost = parts_cost + subassembly_cost
        return total_cost


    def __str__(self):
        return self.sub_assembly_name


class Assembly(models.Model):
    assembly_name = models.CharField(max_length=50)
    assembly_part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True)
    supplier = models.ForeignKey('app.Supplier', null=True, blank=True)
    supplier_pn = models.CharField(max_length=50, null=True, blank=True)
    finish = models.ForeignKey('app.FinishTable', null=True, blank=True)
    plating = models.ForeignKey('app.PlatingTable', null=True, blank=True)
    part_list = models.ManyToManyField(Part)
    part_quantity = models.IntegerField(null=True, blank=True)
    subassembly_list = models.ManyToManyField(SubAssembly)
    subassembly_quantity = models.IntegerField(null=True, blank=True)
    assembly_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    cad_file = models.FileField(null=True, blank=True)
    # many of these fields need to be Null=True

    def __str__(self):
        return self.assembly_name


class Project(models.Model):
    project_number = models.AutoField(primary_key=True)
    client = models.ForeignKey('app.Customer')
    project_name = models.CharField(max_length=50)
    products = models.ManyToManyField(Assembly)
    quantity_per_product = models.IntegerField(null=True, blank=True)
    price_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    extended_price_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_project = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    shipping_terms = models.ForeignKey(ShippingTerms, null=True, blank=True)
    expected_delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.product


class Customer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=25, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    orders = models.ManyToManyField(Project)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=25, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    items_supplied = models.ManyToManyField(Part)

    def __str__(self):
        return self.name


class FinishTable(models.Model):
    finish = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    source = models.ForeignKey(Supplier, null=True, blank=True)

    def __str__(self):
        return self.finish


class PlatingTable(models.Model):
    plating = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    source = models.ForeignKey(Supplier, null=True, blank=True)

    def __str__(self):
        return self.plating
