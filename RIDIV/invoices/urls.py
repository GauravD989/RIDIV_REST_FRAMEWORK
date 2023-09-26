from django.urls import path
from invoices import views

urlpatterns = [
    path('invoices/', views.InvoiceListCreateView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoice_details/', views.InvoiceDetailListCreateView.as_view(), name='invoice-detail-list'),
    path('invoice_details/<int:pk>/', views.InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]
