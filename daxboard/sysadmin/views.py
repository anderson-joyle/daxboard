import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from common.fetching import Fetcher as DataFetcher
from common.tokening import TokenManager

from .services.summary import (
    BatchJobErrorSummary,
    BatchJobExecutingSummary,
    BatchJobWaitingSummary,
    BatchJobWithholdSummary,
)

from .services.tables import (
    SqlBlocking,
    SqlLockInfo,
    SqlInfo,
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

    batch_job_error = BatchJobErrorSummary(data_fetcher)
    batch_job_error.fetch_data()

    batch_job_executing = BatchJobExecutingSummary(data_fetcher)
    batch_job_executing.fetch_data()

    batch_job_waiting = BatchJobWaitingSummary(data_fetcher)
    batch_job_waiting.fetch_data()

    batch_job_withhold = BatchJobWithholdSummary(data_fetcher)
    batch_job_withhold.fetch_data()

    print('=========================================> SQL ANALYSES: Comecou',)
    sql_blocking = SqlBlocking(data_fetcher)
    sql_blocking.fetch_data()

    sql_lock_info = SqlLockInfo(data_fetcher)
    sql_lock_info.fetch_data()

    sql_info = SqlInfo(data_fetcher)
    sql_info.fetch_data()

    print('=========================================> BLOCKING: ', len(sql_blocking.get_context_value()))
    print('=========================================> LOCK: ', len(sql_lock_info.get_context_value()))
    print('=========================================> INFO: ', sql_info.get_context_value())



    context[batch_job_error.get_context_key()] = batch_job_error.get_context_value()
    context[batch_job_executing.get_context_key()] = batch_job_executing.get_context_value()
    context[batch_job_waiting.get_context_key()] = batch_job_waiting.get_context_value()
    context[batch_job_withhold.get_context_key()] = batch_job_withhold.get_context_value()


    return render(request, 'sysadmin/index.html', context)