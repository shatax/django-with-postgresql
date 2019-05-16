from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Books
from api_app.serializers import BookSerializer

@api_view(['GET', 'POST'])
def books_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def books_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        book = book.objects.get(pk=pk)
    except book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)