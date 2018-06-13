from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('salesinvoices/', views.sales_invoices),
    path('salesinvoices/<invoice_id>', views.sales_invoice),
    path('salesorders/', views.sales_orders),    
    path('salesorders/<order_id>', views.sales_order),
    path('changecompany/<company>', views.change_company),
]