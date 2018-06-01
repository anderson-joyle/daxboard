from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detailed/opensalesorders/', views.open_sales_orders),
    path('detailed/openpurchorders/', views.open_purch_orders),
    path('detailed/dailybalance/', views.daily_balance),
    path('detailed/metrics/', views.metrics),
    path('salesinvoice/<invoice_id>', views.sales_invoice),
    path('salesorder/<order_id>', views.sales_order),
]