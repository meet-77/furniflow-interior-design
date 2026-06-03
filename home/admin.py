from django.contrib import admin
from home.models import * 
# Register your models here.

@admin.register(Herosection)
class HeorAdmin(admin.ModelAdmin):
    list_display = ['hero_name'] 

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_title' , 'product_price' , 'product_image']
admin.site.register(Product ,ProductAdmin )
admin.site.register(Product_detail)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['Service_name' , 'Service_image']
admin.site.register(Service_image)

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display =['Design_name']
admin.site.register(Design_image)
admin.site.register(Design_subtext)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['About_title', 'About_image']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['Blog_title']   