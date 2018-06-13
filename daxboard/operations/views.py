import requests
import pickle
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages

from .services.charts import OperationChartSimple

from .services.summary import (
    SalesOrdersSummary,
    PurchOrdersSummary,
    FreeTextInvoiceSummary,
)

from .services.tables import (
    LatestSalesOrders,
    LatestSalesInvoices,
    UserInfoService,
)

from common.tables import (
    LegalEntities,
)

from common.fetching import Fetcher as DataFetcher
from common.tokening import TokenManager

# Create your views here.
def change_company(request, company):
    token_manager = TokenManager()
    token_manager.unpack(request.session['token_pack'])

    data_fetcher = DataFetcher(token_manager)

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    entity_ids = []
    for entity in legal_entities.get_context_value():
        entity_ids.append(entity['LegalEntityId'])
        
    if company in entity_ids:
        request.session['cur_ext'] = company
    else:
        messages.add_message(request, messages.ERROR, 'Company {0} does not exist.'.format(company))

    return redirect('/operations')

def index(request):
    """
    Some description here.
    """
    if not request.user.is_authenticated:
        return redirect('/login')

    context = {}    
    context['resource_url'] = request.session.get('resource')

    token_manager = TokenManager()
    token_manager.unpack(request.session['token_pack'])

    data_fetcher = DataFetcher(token_manager)

    user_info_service = UserInfoService(data_fetcher)
    user_info_service.fetch_data()

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    if not request.session.get('cur_ext'):
        request.session['cur_ext'] = user_info_service.get_context_value()['Company']

    sales_orders_summary = SalesOrdersSummary(data_fetcher)
    sales_orders_summary.extra_filters(dataAreaId=request.session['cur_ext'])
    sales_orders_summary.fetch_data()

    purch_orders_summary = PurchOrdersSummary(data_fetcher)
    purch_orders_summary.extra_filters(dataAreaId=request.session['cur_ext'])
    purch_orders_summary.fetch_data()

    free_text_invoice_summary = FreeTextInvoiceSummary(data_fetcher)
    free_text_invoice_summary.extra_filters(dataAreaId=request.session['cur_ext'])
    free_text_invoice_summary.fetch_data()

    latest_sales_order = LatestSalesOrders(data_fetcher)    
    latest_sales_order.extra_filters(dataAreaId=request.session['cur_ext'])
    latest_sales_order.fetch_data()

    latest_sales_invoice = LatestSalesInvoices(data_fetcher)
    latest_sales_invoice.extra_filters(dataAreaId=request.session['cur_ext'])
    latest_sales_invoice.fetch_data()

    context[sales_orders_summary.get_context_key()] = sales_orders_summary.get_context_value()
    context[purch_orders_summary.get_context_key()] = purch_orders_summary.get_context_value()
    context[free_text_invoice_summary.get_context_key()] = free_text_invoice_summary.get_context_value()
    context[latest_sales_order.get_context_key()] = latest_sales_order.get_context_value()
    context[latest_sales_invoice.get_context_key()] = latest_sales_invoice.get_context_value()
    context[legal_entities.get_context_key()] = legal_entities.get_context_value()
    context[user_info_service.get_context_key()] = user_info_service.get_context_value()

    context['cur_ext'] = request.session['cur_ext']

    return render(request, 'operations/index.html', context)

def sales_invoice(request, invoice_id):
    token_manager = TokenManager()
    token_manager.unpack(request.session['token_pack'])

    data_fetcher = DataFetcher(token_manager)

    user_info_service = UserInfoService(data_fetcher)
    user_info_service.fetch_data()

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    context = {}
    context['sales_invoice_id'] = invoice_id
    context['cur_ext'] = request.session['cur_ext']
    context[legal_entities.get_context_key()] = legal_entities.get_context_value()
    context[user_info_service.get_context_key()] = user_info_service.get_context_value()
    
    return render(request, 'operations/sales_invoice.html', context)

def sales_invoices(request):    
    token_manager = TokenManager()
    token_manager.unpack(request.session['token_pack'])

    data_fetcher = DataFetcher(token_manager)

    user_info_service = UserInfoService(data_fetcher)
    user_info_service.fetch_data()

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    context = {}
    context['cur_ext'] = request.session['cur_ext']
    context[legal_entities.get_context_key()] = legal_entities.get_context_value()
    context[user_info_service.get_context_key()] = user_info_service.get_context_value()

    return render(request, 'operations/sales_invoices.html', {})

def sales_order(request, order_id):
    token_manager = TokenManager()
    token_manager.unpack(request.session['token_pack'])

    data_fetcher = DataFetcher(token_manager)

    user_info_service = UserInfoService(data_fetcher)
    user_info_service.fetch_data()

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    context = {}
    context['sales_order_id'] = order_id
    context['cur_ext'] = request.session['cur_ext']
    context[legal_entities.get_context_key()] = legal_entities.get_context_value()
    context[user_info_service.get_context_key()] = user_info_service.get_context_value()
    
    return render(request, 'operations/sales_order.html', context)
    
def sales_orders(request):    
    token_manager = TokenManager()
    token_manager.unpack(request.session['token_pack'])

    data_fetcher = DataFetcher(token_manager)

    user_info_service = UserInfoService(data_fetcher)
    user_info_service.fetch_data()

    legal_entities = LegalEntities(data_fetcher)
    legal_entities.fetch_data()

    context = {}
    context['cur_ext'] = request.session['cur_ext']
    context[legal_entities.get_context_key()] = legal_entities.get_context_value()
    context[user_info_service.get_context_key()] = user_info_service.get_context_value()

    return render(request, 'operations/sales_orders.html', {})

def daily_balance(request):    
    return render(request, 'operations/daily_balance.html', {})

def metrics(request):    
    return render(request, 'operations/metrics.html', {})