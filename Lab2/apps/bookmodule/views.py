from django.shortcuts import render


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
