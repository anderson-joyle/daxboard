import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from common.fetching import Fetcher as DataFetcher
from common.tokening import TokenManager

from .services.summary import (
    OpenCasesSummary,
    OpenLeadsSummary,
    ActiveOpportunitiesSummary,
    BackendSalesOrdersSummary,
)

from .services.tables import (
    LatestSalesOrders,
    LatestWonOpportunities,
)

from common.tables import (
    LegalEntities,
)

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

    legak_entities = LegalEntities(data_fetcher)
    legak_entities.fetch_data()

    open_cases_summary = OpenCasesSummary(data_fetcher)
    open_cases_summary.fetch_data()

    open_leads_summary = OpenLeadsSummary(data_fetcher)
    open_leads_summary.fetch_data()

    active_opportunities_summary = ActiveOpportunitiesSummary(data_fetcher)
    active_opportunities_summary.fetch_data()

    backend_sales_order_summary = BackendSalesOrdersSummary(data_fetcher)
    backend_sales_order_summary.fetch_data()

    latest_sales_order_summary = LatestSalesOrders(data_fetcher)
    latest_sales_order_summary.fetch_data()

    latest_won_opportunities_summary = LatestWonOpportunities(data_fetcher)
    latest_won_opportunities_summary.fetch_data()

    context[legak_entities.get_context_key()] = legak_entities.get_context_value()
    context[open_cases_summary.get_context_key()] = open_cases_summary.get_context_value()
    context[open_leads_summary.get_context_key()] = open_leads_summary.get_context_value()
    context[active_opportunities_summary.get_context_key()] = active_opportunities_summary.get_context_value()
    context[backend_sales_order_summary.get_context_key()] = backend_sales_order_summary.get_context_value()
    context[latest_sales_order_summary.get_context_key()] = latest_sales_order_summary.get_context_value()
    context[latest_won_opportunities_summary.get_context_key()] = latest_won_opportunities_summary.get_context_value()

    return render(request, 'sales/index.html', context)