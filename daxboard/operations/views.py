import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    For test purposes only.
    """
    if not request.user.is_authenticated:
        return redirect('/')

    context = {}    

    resource_url = request.session['token_json']['resource']

    headers = {
        'Authorization': '{0} {1}'.format(request.session['token_json']['token_type'], request.session['token_json']['access_token']),
        'OData-MaxVersion': '4.0',
        'OData-Version': '4.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
    }

    # Legal entities
    resource_legal_entites = resource_url + '/data/' + 'LegalEntities'
    resource_customer_groups = resource_url + '/data/' + 'CustomerGroups'
    resource_free_text_invoices = resource_url + '/data/' + 'FreeTextInvoices'
    resource_sales_order_headers = resource_url + '/data/' + 'SalesOrderHeaders'
    resource_service_sql_diagnostic = resource_url + '/api/services/UserSessionService/AifUserSessionService/GetUserSessionInfo'

    response = requests.post(resource_service_sql_diagnostic, headers=headers)

    if response.status_code == 200:
        sql_diagnostic_json = response.json()
        context['sql_diagnostic'] = sql_diagnostic_json

    response = requests.get(resource_legal_entites, headers=headers)

    if response.status_code == 200:
        legal_entities_json = response.json()['value']
        context['entities'] = legal_entities_json

    response = requests.get(resource_customer_groups, headers=headers)

    if response.status_code == 200:
        customer_groups_json = response.json()['value']
        if len(customer_groups_json) > 10:
            customer_groups_json = customer_groups_json[:10]
        context['customer_groups'] = customer_groups_json

    response = requests.get(resource_free_text_invoices, headers=headers)

    if response.status_code == 200:
        free_text_invoices_json = response.json()['value']
        if len(free_text_invoices_json) > 10:
            free_text_invoices_json = free_text_invoices_json[:10]
        context['free_text_invoices'] = free_text_invoices_json

    response = requests.get(resource_sales_order_headers, headers=headers)

    if response.status_code == 200:
        sales_order_headers_json = response.json()['value']
        context['sales_order_headers'] = sales_order_headers_json
        context['sales_order_headers_counter'] = len(sales_order_headers_json)
        

    context['is_authenticated'] = request.user.is_authenticated
    context['resource_url'] = resource_url
    context['tenant'] = request.session.get('tenant')

    return render(request, 'operations/index.html', context)