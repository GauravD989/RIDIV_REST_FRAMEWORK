from django.contrib import admin
from invoices.models import Invoice, InvoiceDetail
# Register your models here.

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)