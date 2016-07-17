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


class FinishTable(models.Model):
    finish = models.CharField(max_length=20)
    description = models.TextField()
    source = models.ForeignKey(Supplier)

    def __str__(self):
        return self.finish


class PlatingTable(models.Model):
    plating = models.CharField(max_length=20)
    description = models.TextField()
    source = models.ForeignKey(Supplier)

    def __str__(self):
        return self.plating


class ShippingTerms(models.Model):
    shipping_type = models.CharField(max_length=20)
    description = models.TextField()
    preferred_shipper = models.CharField(max_length=30)

    def __str__(self):
        return self.shipping_type


class Project(models.Model):
    product = models.ManytoMany(Assemlby)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer)
    price = models.ForeignKey(Assembly)
    shipping_address = models.TextField()
    shipping_terms = models.ForeignKey(ShippingTerms)
    expected_delivery = models.DateField()

    def __str__(self):
        return self.product


class Customer(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name


class Part(models.Model):
    part_name = models.CharField(max_length=30)
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    supplier = models.ForeignKey(Supplier)
    supplier_pn = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=30)
    finish = models.ForeignKey(FinishTable)
    plating = models.ForeignKey(PlatingTable)
    uom = models.CharField(max_length=15)
    cost_per_unit = models.DecimalField(max_digits=None, decimal_places=2)
    part_url = models.URLField()
    notes = models.TextField()
    cad_file = models.FileField()
    image = models.ImageField()
    # many of these fields need to be Null=True

    def __str__(self):
        return self.part_name


class Assembly(models.Model):
    assembly_name = models.CharField(max_length=30)
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    supplier = models.ForeignKey(Supplier)
    supplier_pn = models.CharField(max_length=50)
    list_of_parts = models.ManyToManyField()
    list_of_assemblies = models.ManyToManyField()
    quantity = models.IntegerField()
    extended_price = models.DecimalField(max_digits=None, decimal_places=2)
    notes = models.TextField()
    cad_file = models.FileField()
    # many of these fields need to be Null=True

    def __str__(self):
        return self.assembly_name


class Supplier(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    items_supplied = models.ManyToManyField(Part)

    def __str__(self):
        return self.name
