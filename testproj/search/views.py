from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from wagtail.models import Page
from wagtail.search.models import Query
from home.models import *


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )


def index(request):
    return render(request, 'search/index.html')

def form(request):
    if(request.method=='POST'):
        saverecord = Values()
        saverecord.lastname = request.POST.get("lastname")
        lastname = request.POST.get("lastname")
        saverecord.save()
    return render(request, 'search/submitted.html', {'lastname': lastname})
