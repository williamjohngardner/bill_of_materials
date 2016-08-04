from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
    user = models.ForeignKey("auth.User")
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class SubCategory(models.Model):
    user = models.ForeignKey("auth.User")
    category = models.ForeignKey(Category)
    subcategory = models.CharField(max_length=30)

    def __str__(self):
        return self.subcategory


class ShippingTerms(models.Model):
    user = models.ForeignKey("auth.User")
    shipping_type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    preferred_shipper = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.shipping_type


class Part(models.Model):
    user = models.ForeignKey("auth.User")
    part_name = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category)
    sub_category = models.ForeignKey(SubCategory)
    manufacturer = models.ForeignKey('app.Supplier', null=True, blank=True)
    manufacturer_pn = models.CharField(max_length=50, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    finish = models.ForeignKey('app.FinishTable', null=True, blank=True)
    plating = models.ForeignKey('app.PlatingTable', null=True, blank=True)
    uom = models.CharField(max_length=15, null=True, blank=True)
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
        return self.part.part_name


class AssemblyQuantity(models.Model):
    part = models.ForeignKey(Part, null=True, blank=True)
    subassembly = models.ForeignKey('app.SubAssembly', null=True, blank=True)
    quantity = models.IntegerField()
    assembly = models.ForeignKey('app.Assembly', null=True, blank=True)

    @property
    def sub_cost(self):
        if not self.part:
            return 0
        cost = self.part.unit_cost * self.quantity
        return cost

    @property
    def cost(self):
        if not self.part:
            return 0
        cost = self.part.unit_cost * self.quantity
        return cost

    def __str__(self):
        return self.assembly.assembly_name


class SubAssembly(models.Model):
    user = models.ForeignKey("auth.User")
    sub_assembly_name = models.CharField(max_length=50)
    sub_assembly_number = models.CharField(max_length=50, null=True, blank=True)
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
    image = models.ImageField(upload_to="image_files", null=True, blank=True, verbose_name="Part Image")


    @property
    def cost(self):
        cost = 0
        for subassemblyquantity in self.subassemblyquantity_set.all():
            cost += subassemblyquantity.cost
        return cost

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://cdn3.iconfinder.com/data/icons/smoothfill-action/30/action_088-no_camera-capture-picture-image-photo-128.png"

    def __str__(self):
        return self.sub_assembly_name


class Assembly(models.Model):
    user = models.ForeignKey("auth.User")
    assembly_name = models.CharField(max_length=50)
    assembly_part_number = models.CharField(max_length=50, null=True, blank=True)
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
    image = models.ImageField(upload_to="image_files", null=True, blank=True, verbose_name="Part Image")


    @property
    def cost(self):
        cost = 0
        for assembly_quantity in self.assemblyquantity_set.all():
            cost += assembly_quantity.cost
            subassembly = assembly_quantity.subassembly
            if subassembly:
                cost += subassembly.cost * assembly_quantity.quantity
        return cost

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://cdn3.iconfinder.com/data/icons/smoothfill-action/30/action_088-no_camera-capture-picture-image-photo-128.png"

    def __str__(self):
        return self.assembly_name


class ProjectQuantity(models.Model):
    assembly = models.ForeignKey('app.Assembly', null=True, blank=True)
    quantity = models.IntegerField()
    price_per_assembly = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    project = models.ForeignKey('app.Project', null=True, blank=True)



class Project(models.Model):
    user = models.ForeignKey("auth.User")
    project_number = models.AutoField(primary_key=True)
    client = models.ForeignKey('app.Customer')
    project_name = models.CharField(max_length=50)
    price_per_project = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    shipping_terms = models.ForeignKey(ShippingTerms, null=True, blank=True)
    expected_delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.project_name

class Customer(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True )
    title = models.CharField(max_length=30, null=True, blank=True)
    company_name = models.CharField(max_length=25, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email_address = models.CharField(max_length=60, null=True, blank=True)
    twitter_account = models.CharField(max_length=25, null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.company_name


class Supplier(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True )
    title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email_address = models.CharField(max_length=60, null=True, blank=True)
    twitter_account = models.CharField(max_length=25, null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    street_address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.company_name


class FinishTable(models.Model):
    user = models.ForeignKey("auth.User")
    finish = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    source = models.ForeignKey(Supplier, null=True, blank=True)
    image = models.ImageField(upload_to="image_files", null=True, blank=True, verbose_name="Part Image")

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://cdn3.iconfinder.com/data/icons/smoothfill-action/30/action_088-no_camera-capture-picture-image-photo-128.png"

    def __str__(self):
        return self.finish


class PlatingTable(models.Model):
    user = models.ForeignKey("auth.User")
    plating = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    source = models.ForeignKey(Supplier, null=True, blank=True)

    def __str__(self):
        return self.plating


class UserProfile(models.Model):
    user = models.ForeignKey("auth.User")
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=30, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user_name


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")

    if created:
        UserProfile.objects.create(user=instance)


# @receiver(post_save, sender="auth.User") #every post save will call def User
# def create_token(**kwargs):
#     created = kwargs.get("created")
#     instance = kwargs.get("instance")
#     if created:
#         Token.objects.create(user=instance)
