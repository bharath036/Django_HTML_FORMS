from django.db import models
from django.template.defaultfilters import slugify 

# Create your models here.

#we need to create table

class Contact(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices = (
        ('Male','Male'),
        ('Female','Female'),
    ) , default = 'Male'
    )
    phone_number = models.CharField(max_length=10, null=True,blank=True)
    comment = models.CharField(max_length=100)    
    file = models.FileField(upload_to="files",null=True,blank=True)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    remarks = models.TextField(null=True,blank=True)
    quantity = models.IntegerField()
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="product/files")

    def save(self,*args,**kwargs):
        self.slug = slugify(f"{self.product_name}")
        super(Product,self).save(*args,**kwargs)

    class Meta:
        db_table = "product_table"
