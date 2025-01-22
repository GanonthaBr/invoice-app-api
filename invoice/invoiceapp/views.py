from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Invoice
from .serializers import InvoiceSerializer
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    @action(detail=True, methods=['get'])
    def download_pdf(self, request, pk=None):
        invoice = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.drawString(100, 750, f"Invoice ID: {invoice.id}")
        p.drawString(100, 730, f"Customer: {invoice.client.client_name}")
        p.drawString(100, 710, f"Echeance: {invoice.echeance}")
        y = 690
        for designation in invoice.designations.all():
            p.drawString(100, y, f"Item: {designation.title}, Quantity: {designation.quantity}, Unit Price: {designation.unit_price}, Price: {designation.price}")
            y -= 20
        p.drawString(100, y - 20, f"Total Amount (with tax): {invoice.total_amount}")
        p.showPage()
        p.save()

        return response