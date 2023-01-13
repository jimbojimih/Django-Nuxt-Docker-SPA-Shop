from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Category, SubCategory, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


class ImagesTabularInline(admin.TabularInline):
    model = Image
    extra = 2   
    min_num = 1
    readonly_fields = ['image_preview',]
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='250' />".format(
                    obj.image.url))
        return None

        
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):    
    inlines = [ImagesTabularInline, ]
    list_display = ['name', 'id', 'price', 'available', 'get_image', ]     
    fields = ['sub_category', 'id', 'name', 'description', 'price', 
              'available', 'created', 'updated',]
    readonly_fields = ['id', 'created', 'updated']
    list_filter = ['available', 'price', ]     

    def get_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            return mark_safe("<img src='{}' width='150' />".format(
                    first_image.image.url))
        return None

    get_image.__name__ = 'Превью'

