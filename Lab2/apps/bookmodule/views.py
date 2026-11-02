from django.db.models import Avg, Count, Max, Min, Q, Sum
from django.shortcuts import render

from .models import Address, Book, Publisher


def index(request):
    """Render the library home page."""
    return render(request, "bookmodule/index.html")


def index2(request, val1=0):
    """Display an integer captured from the URL path."""
    return render(request, "bookmodule/index2.html", {"value1": val1})


def viewbook(request, bookId):
    """Display the details for one of the sample books."""
    books = {
        123: {
            "id": 123,
            "title": "Internet and World Wide Web How to Program",
            "author": "P. Deitel and H. Deitel",
            "image": "book1.svg",
            "description": "A clear introduction to Internet and web programming for introductory and intermediate courses.",
        },
        456: {
            "id": 456,
            "title": "C++ How to Program",
            "author": "P. Deitel and H. Deitel",
            "image": "book2.svg",
            "description": "A practical guide to modern C++ programming and object-oriented design.",
        },
        789: {
            "id": 789,
            "title": "Learning Python",
            "author": "Mark Lutz",
            "image": "book3.svg",
            "description": "A beginner-friendly reference for learning the Python programming language.",
        },
    }
    return render(request, "bookmodule/one_book.html", {"book": books.get(bookId)})


def list_books(request):
    """Render the library catalogue."""
    books = [
        {"id": 123, "title": "Internet and World Wide Web How to Program", "image": "book1.svg"},
        {"id": 456, "title": "C++ How to Program", "image": "book2.svg"},
        {"id": 789, "title": "Learning Python", "image": "book3.svg"},
    ]
    return render(request, "bookmodule/list_books.html", {"books": books})


def aboutus(request):
    """Render the library about page."""
    return render(request, "bookmodule/aboutus.html")


def html5_links(request):
    return render(request, "bookmodule/html5_links.html")


def html5_formatting(request):
    return render(request, "bookmodule/html5_formatting.html")


def html5_listing(request):
    return render(request, "bookmodule/html5_listing.html")


def html5_tables(request):
    return render(request, "bookmodule/html5_tables.html")


def __getBooksList():
    book1 = {"id": 12344321, "title": "Continuous Delivery", "author": "J. Humble and D. Farley"}
    book2 = {"id": 56788765, "title": "Reversing: Secrets of Reverse Engineering", "author": "E. Eilam"}
    book3 = {"id": 43211234, "title": "The Hundred-Page Machine Learning Book", "author": "Andriy Burkov"}
    return [book1, book2, book3]


def search(request):
    """Display the search form and handle its submitted search criteria."""
    if request.method == "POST":
        string = request.POST.get("keyword", "").lower()
        isTitle = request.POST.get("option1")
        isAuthor = request.POST.get("option2")
        newBooks = []

        for item in __getBooksList():
            contained = False
            if isTitle and string in item["title"].lower():
                contained = True
            if not contained and isAuthor and string in item["author"].lower():
                contained = True
            if contained:
                newBooks.append(item)
        return render(request, "bookmodule/bookList.html", {"books": newBooks})

    return render(request, "bookmodule/search.html")


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains="and")
    return render(request, "bookmodule/bookList.html", {"books": mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(
        title__icontains="and"
    ).filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, "bookmodule/bookList.html", {"books": mybooks})
    else:
        return render(request, "bookmodule/index.html")


def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, "bookmodule/lab8_books.html", {"books": books, "task": 1})


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains="co") | Q(author__icontains="co"))
    )
    return render(request, "bookmodule/lab8_books.html", {"books": books, "task": 2})


def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(Q(title__icontains="co") | Q(author__icontains="co"))
    )
    return render(request, "bookmodule/lab8_books.html", {"books": books, "task": 3})


def lab8_task4(request):
    books = Book.objects.order_by("title")
    return render(request, "bookmodule/lab8_books.html", {"books": books, "task": 4})


def lab8_task5(request):
    summary = Book.objects.aggregate(
        number_of_books=Count("id"),
        total_price=Sum("price"),
        average_price=Avg("price"),
        maximum_price=Max("price"),
        minimum_price=Min("price"),
    )
    return render(request, "bookmodule/lab8_summary.html", {"summary": summary})


def lab8_task7(request):
    cities = Address.objects.annotate(number_of_students=Count("student"))
    return render(request, "bookmodule/lab8_cities.html", {"cities": cities})


def lab9_task1(request):
    total_books = Book.objects.aggregate(total_quantity=Sum("quantity"))["total_quantity"] or 0
    books = Book.objects.all()
    for book in books:
        book.availability_percentage = (book.quantity / total_books * 100) if total_books else 0
    return render(request, "bookmodule/lab9_books.html", {"books": books, "task": 1})


def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_book_stock=Sum("book__quantity"))
    return render(request, "bookmodule/lab9_publishers.html", {"publishers": publishers, "task": 2})


def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min("book__pubdate"))
    return render(request, "bookmodule/lab9_publishers.html", {"publishers": publishers, "task": 3})


def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        average_price=Avg("book__price"),
        minimum_price=Min("book__price"),
        maximum_price=Max("book__price"),
    )
    return render(request, "bookmodule/lab9_publishers.html", {"publishers": publishers, "task": 4})


def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        highly_rated_books=Count("book", filter=Q(book__rating__gte=4))
    )
    return render(request, "bookmodule/lab9_publishers.html", {"publishers": publishers, "task": 5})


def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        matching_books=Count(
            "book", filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )
    return render(request, "bookmodule/lab9_publishers.html", {"publishers": publishers, "task": 6})
