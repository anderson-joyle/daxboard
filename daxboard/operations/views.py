import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .services.charts import OperationChartSimple
from .services.summary import (
    SalesOrdersSummary,
    PurchOrdersSummary
)
from .services.tables import (
    LatestSalesOrders,
    LatestSalesInvoices,
    LegalEntities,
    UserInfoService,
)

from common.fetching import Fetcher as DataFetcher
from common.tokening import TokenManager

# Create your views here.
def index(request):
    """
    Some description here.
    """
    if not request.user.is_authenticated:
        return redirect('/')

    context = {}    
    context['resource_url'] = request.session.get('resource')

    token_manager = TokenManager(
                        resource=request.session.get('resource'),
                        tenant=request.session.get('tenant'),
                        client_id=request.session.get('client_id'),
                        client_secret=request.session.get('client_secret'),
                        username=request.session.get('username'),
                        password=request.session.get('password')
                    )

    data_fetcher = DataFetcher(token_manager)

    sales_orders_summary = SalesOrdersSummary(data_fetcher)
    sales_orders_summary.fetch_data()

    purch_orders_summary = PurchOrdersSummary(data_fetcher)
    purch_orders_summary.fetch_data()

    latest_sales_order = LatestSalesOrders(data_fetcher)
    latest_sales_order.fetch_data()

    latest_sales_invoice = LatestSalesInvoices(data_fetcher)
    latest_sales_invoice.fetch_data()

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    user_info_service = UserInfoService(data_fetcher)
    user_info_service.fetch_data()

    context[sales_orders_summary.get_context_key()] = sales_orders_summary.get_context_value()
    context[purch_orders_summary.get_context_key()] = purch_orders_summary.get_context_value()
    context[latest_sales_order.get_context_key()] = latest_sales_order.get_context_value()
    context[latest_sales_invoice.get_context_key()] = latest_sales_invoice.get_context_value()
    context[legal_entities.get_context_key()] = legal_entities.get_context_value()

    return render(request, 'operations/index.html', context)

def sales_invoice(request, invoice_id):
    context = {
        'sales_invoice_id': invoice_id
    }
    
    return render(request, 'operations/sales_invoice.html', context)

def sales_order(request, order_id):
    context = {
        'sales_order_id': order_id
    }
    
    return render(request, 'operations/sales_order.html', context)

def open_sales_orders(request):    
    return render(request, 'operations/open_sales_orders.html', {})

def open_purch_orders(request):    
    return render(request, 'operations/open_purch_orders.html', {})

def daily_balance(request):    
    return render(request, 'operations/daily_balance.html', {})

def metrics(request):    
    return render(request, 'operations/metrics.html', {})