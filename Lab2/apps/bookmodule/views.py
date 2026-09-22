from django.shortcuts import render


def index(request):
    """Render the book module welcome page."""
    name = request.GET.get("name") or "world"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    """Display an integer captured from the URL path."""
    return render(request, "bookmodule/index2.html", {"value1": val1})


def viewbook(request, bookId):
    """Display the details for one of the sample books."""
    books = {
        123: {
            "id": 123,
            "title": "Continuous Delivery",
            "author": "J. Humble and D. Farley",
        },
        456: {
            "id": 456,
            "title": "Secrets of Reverse Engineering",
            "author": "E. Eilam",
        },
    }
    return render(request, "bookmodule/show.html", {"book": books.get(bookId)})
