from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from django.utils import simplejson
from news.models import News


def index(request):

    news_list = News.objects.filter(active=True).order_by('-updated_date')[:3]
    context = RequestContext(request, {
        'news':news_list,
    })
    return render_to_response('news_list.html', context)

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    if not news.active:
        raise Http404
    context = RequestContext(request, {
        'news':news,
    })
    return render_to_response('news_detail.html', context)

def page(request, page):
    news_list = News.objects.filter(active=True).order_by('-updated_date')
    paginator = Paginator(news_list, 3)
    data_format_list = list()
    try:
        news_paginated = paginator.page(page)
    except PageNotAnInteger:
        news_paginated = False
    except EmptyPage:
        news_paginated = False
    if news_paginated:
        for news in news_paginated:
            data = {}
            data['title'] = news.title
            data['quick_description'] = news.quick_description
            data['updated_date'] = news.updated_date.strftime('%d/%m/%Y')
            data['slug'] = news.slug
            data_format_list.append(data)
        response_data = simplejson.dumps(data_format_list)
    else:
        response_data = False
    return HttpResponse( response_data, mimetype = 'application/json' )
