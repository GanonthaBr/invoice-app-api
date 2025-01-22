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
    client_address = models.CharField(max_length=100)
class Facture(models.Model):
    title = models.TextField()
    topic = models.TextField()
    number = models.CharField(max_length=100)
    echeance = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    unit_price = models.DecimalField()
    quantity = models.DecimalField()
    designation_details = models.TextField()
    tax = models.IntegerField()
    type_tax = models.CharField(max_length=100)
    payment_mode = models.TextField()