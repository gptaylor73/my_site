from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Max, Min


from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-rating')  # sort by rating -
    # descending
    num_books = books.count()
    aggs_rating = books.aggregate(Avg('rating'), Max('rating'))  # returns a
    # dictionary
    return render(request, 'book_store/index.html',
                  {'books': books,
                   'total_number_of_books': num_books,
                   'aggs_rating': aggs_rating})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_store/book_detail.html',
                  {
                      'title': book.title,
                      'author': book.author,
                      'rating': book.rating,
                      'is_bestseller': book.is_bestselling
                  })
