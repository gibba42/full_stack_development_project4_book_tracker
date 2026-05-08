from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm

from .models import Book
from .services import search_open_library

def index(request):
    return render(request, "book_tracker/index.html")


def book_search(request):

    query = request.GET.get("q", "").strip()
    sort_by = request.GET.get("sort", "")
    has_cover = request.GET.get("has_cover") == "on"

    results = []
    error = None

    if query:
        search_response = search_open_library(
            query=query,
            sort_by=sort_by,
            has_cover=has_cover
        )

        results = search_response["results"]
        error = search_response["error"]

        if error:
            messages.error(request, error)
        elif not results:
            messages.info(request, "No books matched your search.")

    context = {
        "query": query,
        "results": results,
        "sort_by": sort_by,
        "has_cover": has_cover,
        "error": error,
    }

    return render(request, "book_tracker/book_search.html", context)


@login_required
def add_book_to_library(request):

    if request.method != "POST":
        messages.error(request, "Invalid request.")
        return redirect("book_search")

    open_library_key = request.POST.get("open_library_key")
    title = request.POST.get("title")
    author = request.POST.get("author", "")
    first_publish_year = request.POST.get("first_publish_year") or None
    cover_id = request.POST.get("cover_id") or None
    isbn = request.POST.get("isbn", "")

    if not open_library_key or not title:
        messages.error(request, "Book details were missing. Please try again.")
        return redirect("book_search")

    try:
        Book.objects.create(
            user=request.user,
            open_library_key=open_library_key,
            title=title,
            author=author,
            first_publish_year=first_publish_year,
            cover_id=cover_id,
            isbn=isbn,
        )
        messages.success(request, f'"{title}" was added to your library.')
    except IntegrityError:
        messages.info(request, f'"{title}" is already in your library.')

    return redirect("my_library")

@login_required
def my_library(request):
    books = Book.objects.filter(user=request.user)

    return render(
        request,
        "book_tracker/my_library.html",
        {"books": books}
    )

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)

    return render(
        request,
        "book_tracker/book_detail.html",
        {"book": book}
    )

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect("book_detail", book_id=book.id)

    else:
        form = BookForm(instance=book)

    return render(
        request,
        "book_tracker/book_form.html",
        {
            "form": form,
            "book": book,
        }
    )
    
@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, user=request.user)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book removed from your library.")
        return redirect("my_library")
        
    return render(
        request,
        "book_tracker/book_confirm_delete.html",
        {"book": book}
    )