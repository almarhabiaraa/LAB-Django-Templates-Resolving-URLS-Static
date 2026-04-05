# Imports
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
# Logic of the view or templates to be rendered will be here

def home_view(request : HttpRequest):
    return render(request, "main/home.html")

def terms_view(request : HttpRequest):
    return render(request, "main/terms.html")

def search(request):
    query = request.GET.get('q')

    context = {
        'query': query
    }

    return render(request, 'main/search.html', context)