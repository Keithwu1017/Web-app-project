from django.shortcuts import get_object_or_404, render
from .models import PictureBook

def book_list(request):
    books = PictureBook.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(PictureBook, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def books_by_tag(request, tag_slug):
    books = PictureBook.objects.filter(tags__name__in=[tag_slug])
    return render(request, 'library/book_list.html', {'books': books})