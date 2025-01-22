from .models import Client, Invoice, Designation
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        

class DesignationSerializer(ModelSerializer):
    designation_price = SerializerMethodField()
    class Meta:
        model = Designation
        fields = ['designation_title','designation_details','designation_unit_price','designation_quantity','designation_price']
    def get_designation_price(self,obj):
        return obj.designation_unit_price
    
class InvoiceSerializer(ModelSerializer):
    designations = DesignationSerializer(many=True)
    total_amount = SerializerMethodField()
    class Meta:
        model = Invoice
        fields = "__all__"
    
    def get_total_amount(self,obj):
        return obj.total_amount
