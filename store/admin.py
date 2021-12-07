from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProdcutAdmin(admin.ModelAdmin):
        list_display=['title','author','slug','price','in_stock','created','updated']
        list_filter=['in_stock','is_active']
        list_editable=['price','in_stock']
        prepopulated_fields={'slug' : ('title',)}
        
admin.site.register(Product,ProdcutAdmin)


 
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name','slug']
    #prepopulated means the first field will follow whatever the second field insert
    prepopulated_fields={'slug':('category_name',)}
    
    
admin.site.register(Category, CategoryAdmin)