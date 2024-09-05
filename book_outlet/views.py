from django.shortcuts import render, get_object_or_404
from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request, id: int):
    # book = Book.objects.get(id=id)
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book-detail.html", {"book": book})
