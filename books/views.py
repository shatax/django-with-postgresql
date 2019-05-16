from django.http import HttpResponse
from django.template import loader

from .models import Books

def index(request):
    books_list = Books.objects.order_by('-date_added')[:]
    template = loader.get_template('books/home.html')

    context = {
        'books_list': books_list,
    }

    return HttpResponse(template.render(context, request))

def detail(request, book_id):
    return HttpResponse("You are looking at book %s" % book_id)