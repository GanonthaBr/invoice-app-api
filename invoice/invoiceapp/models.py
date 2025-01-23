from django.db import models

# Create your models here.
'''

        'name',
        'number',
        'echeance',
        'client_name',
        'client_quartier',
        'client_city',
        'client_country',

        'client_phone',
        'client_mail',
        'tax',
        'type_tax',
        'objet',
        'designation_title',
        'mode_paiment',
        'designation_detail',
        'quantity',
        'unit_price',
        'montant_avanc'
'''
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_quartier = models.CharField(max_length=100)
    client_city = models.CharField(max_length=100)
    client_country = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=100)
    client_mail = models.EmailField(max_length=100)
   
class Invoice(models.Model):
    topic = models.TextField()
    number = models.CharField(max_length=100)
    echeance = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tax = models.IntegerField()
    type_tax = models.CharField(max_length=100)
    payment_mode = models.TextField()

    def save(self,*args, **kwargs):

        if not self.number:
            last_invoice = Invoice.objects.all().order_by('id').last()
            if last_invoice:
                self.number = str(int(last_invoice.number) + 1)
            else:
                self.number = '1'
        super().save(*args,**kwargs)
    @property
    def total_amount(self):
        total = sum(designation.designation_price for designation in self.designations.all())
        total_with_tax = total + (total * self.tax/100)
        return total_with_tax
    
class Designation(models.Model):
    invoice = models.ForeignKey(Invoice,related_name='designations',on_delete=models.CASCADE)
    designation_title = models.TextField()
    designation_details = models.TextField()
    designation_unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    designation_quantity = models.IntegerField()

    @property
    def designation_price(self):
        return self.designation_unit_price * self.designation_quantity