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
    cad_file = models.FileField(upload_to="cad_files", null=True, blank=True)
    image = models.ImageField(upload_to="image_files", null=True, blank=True, verbose_name="Part Image")

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://cdn3.iconfinder.com/data/icons/smoothfill-action/30/action_088-no_camera-capture-picture-image-photo-128.png"

    def __str__(self):
        return self.part_name


class SubAssemblyQuantity(models.Model):
    part = models.ForeignKey(Part)
    quantity = models.IntegerField()
    assembly = models.ForeignKey('app.SubAssembly')

    @property
    def cost(self):
        cost = self.part.unit_cost * self.quantity
        return cost

    def __str__(self):
        return self.part


class AssemblyQuantity(models.Model):
    part = models.ForeignKey(Part, null=True, blank=True)
    subassembly = models.ForeignKey('app.SubAssembly', null=True, blank=True)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    assembly = models.ForeignKey('app.Assembly', null=True, blank=True)

    @property
    def subassembly_cost(self):
        cost = self.subassembly.cost
        return cost

    @property
    def assembly_cost(self):
        cost = self.part.unit_cost * self.quantity
        return self.cost

    def __str__(self):
        return ""


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
    subassembly_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    cad_file = models.FileField(upload_to="cad_files", null=True, blank=True)

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
    assembly_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    cad_file = models.FileField(upload_to="cad_files", null=True, blank=True)



class ProjectQuantity(models.Model):
    assembly = models.ForeignKey('app.Assembly', null=True, blank=True)
    quantity = models.IntegerField()
    price_per_assembly = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    project = models.ForeignKey('app.Project', null=True, blank=True)



class Project(models.Model):
    project_number = models.AutoField(primary_key=True)
    client = models.ForeignKey('app.Customer')
    project_name = models.CharField(max_length=50)
    # products = models.ForeignKey(Assembly, null=True, blank=True)
    # quantity_per_product = models.IntegerField(null=True, blank=True)
    # price_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # extended_price_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_project = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    shipping_terms = models.ForeignKey(ShippingTerms, null=True, blank=True)
    expected_delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.project_name


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True )
    title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    twitter_account = models.CharField(max_length=25, null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True )
    title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    twitter_account = models.CharField(max_length=25, null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)

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
