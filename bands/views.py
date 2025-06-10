'''
    AUTHOR : Angad Dogra
    DATE
'''


from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Company  # Your bands model
from .models import Actor  # Your sakila models

def combined_view(request):
    # Bands data
    bands_queryset = Company.objects.all().order_by('-date')
    
    # Sakila data
    actors_queryset = Actor.objects.using('sakila').all()[:10]  # Limit to 10 actors

    # Pagination for bands data
    paginator = Paginator(bands_queryset, 25)  # Show 25 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'bands_data': page_obj,
        'sakila_actors': actors_queryset,
        'page_obj': page_obj,
    }
    
    return render(request, 'index.html', context)