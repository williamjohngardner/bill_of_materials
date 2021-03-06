from django.contrib import admin

from app.models import (Category, SubCategory, ShippingTerms, Part, Assembly,
SubAssembly, Supplier, Customer, FinishTable, PlatingTable, Project, ProjectQuantity, SubAssemblyQuantity, AssemblyQuantity)


admin.site.register(Category)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'category')

admin.site.register(SubCategory, SubCategoryAdmin)

class ShippingTermsAdmin(admin.ModelAdmin):
    list_display = ('shipping_type', 'description', 'preferred_shipper')

admin.site.register(ShippingTerms, ShippingTermsAdmin)

class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'part_name', 'part_number', 'category', 'sub_category', 'manufacturer')

admin.site.register(Part, PartAdmin)

class SubAssemblyAdmin(admin.ModelAdmin):
    list_display = ('sub_assembly_name', 'sub_assembly_number', 'category', 'sub_category', 'mfg_supplier')

admin.site.register(SubAssembly, SubAssemblyAdmin)

class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('assembly_name', 'assembly_part_number', 'category', 'sub_category', 'supplier')

admin.site.register(Assembly, AssemblyAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'company_name', 'phone_number', 'email_address', 'twitter_account', 'web_address', 'street_address', 'city', 'state', 'zip_code', 'country')

admin.site.register(Supplier, SupplierAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'company_name', 'phone_number', 'email_address', 'twitter_account', 'web_address', 'street_address', 'city', 'state', 'zip_code', 'country')

admin.site.register(Customer, CustomerAdmin)

class FinishTableAdmin(admin.ModelAdmin):
    list_display = ('finish', 'description', 'source')

admin.site.register(FinishTable, FinishTableAdmin)

class PlatingTableAdmin(admin.ModelAdmin):
    list_display = ('plating', 'description', 'source')

admin.site.register(PlatingTable, PlatingTableAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_number', 'project_name', 'client', 'price_per_project', 'expected_delivery')

admin.site.register(Project, ProjectAdmin)

class ProjectQuantityAdmin(admin.ModelAdmin):
    list_display = ('assembly', 'quantity', 'price_per_assembly', 'project')

admin.site.register(ProjectQuantity, ProjectQuantityAdmin)

class SubAssemblyQuantityAdmin(admin.ModelAdmin):
    list_display = ('part', 'quantity', 'assembly')

admin.site.register(SubAssemblyQuantity, SubAssemblyQuantityAdmin)

class AssemblyQuantityAdmin(admin.ModelAdmin):
    list_display = ('part', 'subassembly', 'quantity', 'assembly')

admin.site.register(AssemblyQuantity, AssemblyQuantityAdmin)
