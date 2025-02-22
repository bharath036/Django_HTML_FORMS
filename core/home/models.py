from django.db import models
from django.template.defaultfilters import slugify 
from django.db.models.signals import post_save, signal
from django.dispatch import receiver
# Create your models here.

#we need to create table


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


class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_id = models.CharField(max_length=100, null=True,blank = True)
    '''
    age = models.IntegerField()
    gender = models.CharField(max_length=100, choices = (
        ('Male','Male'),
        ('Female','Female'),
    ) , default = 'Male'
    )
    phone_number = models.CharField(max_length=10, null=True,blank=True)
    comment = models.CharField(max_length=100)    
    file = models.FileField(upload_to="files",null=True,blank=True)
    '''

#When ever object is created.., print contact created
@receiver(post_save, sender = Contact)
def contact_obj_created(sender, instance, created, **kwargs):
    print('CONTACT CREATED')
    #if only created this will work 
    #if we wont keep if statement., it causes stackoverflow and recurrsion error
    if created:
        instance.contact_id = f"{(instance.name)}-{str(instance.id).zfill(5)}"
        instance.save()
#We can also trigger email if any operation goes on 

