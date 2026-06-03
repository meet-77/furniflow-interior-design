from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Herosection(models.Model):
    hero_name = models.CharField(max_length=100)
    hero_subtitle = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.hero_name
    
    
class Product_detail(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.TextField(max_length=1000)
       
    def __str__(self):
            return self.title
    
    
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to="product/")
    product_price = models.IntegerField()
    
    def __str__(self):
        return self.product_title
    

    
class Service(models.Model):
    Service_image =  models.ImageField(upload_to="product/")
    Service_name = models.CharField(max_length=200)
    Service_subtitle = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Service_name
    
class Service_image(models.Model):
    image =  models.ImageField(upload_to="product/")

class Design(models.Model):
    Design_name = models.CharField(max_length=200)
    
class Design_image(models.Model):
    images = models.ImageField(upload_to="product/")
    
class Design_subtext(models.Model):
    subtext = models.CharField(max_length=500)
    
class About(models.Model):
    About_title =  models.CharField(max_length=500)
    About_image = models.ImageField(upload_to="product/")
    About_subtext = models.CharField(max_length=500)
    About_more =  models.CharField(max_length=500)
    
    def __str__(self):
        return self.About_title 
    
 
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    image = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.role}"
    
class Blog(models.Model):
    Blog_image =  models.ImageField(upload_to="product/")
    Blog_title =   models.CharField(max_length=500)
    Blog_subtext =   models.CharField(max_length=500)
    
    def __str__(self):
        return self.Blog_title