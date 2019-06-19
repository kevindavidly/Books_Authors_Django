from django.shortcuts import render, redirect
from .models import Book
from .models import Author 

def index(request):
    context = {
        "all_the_books": Book.objects.all()
    }
    return render(request, "books_authors_app/index.html", context)

def book(request, my_val):
    context = {
        "Book": Book.objects.get(id=my_val),
        "Authors": Book.objects.get(id=my_val).authors,
        "allauthors": Author.objects.all(),
    }
    return render(request, "books_authors_app/books.html", context)

def add_book(request):
    new_book = Book.objects.create(title=request.POST["new_title"],desc=request.POST["desc"])
    return redirect("/books/"+str(new_book.id))

def add_author(request):
    new_author= Author.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],notes=request.POST["notes"])
    return redirect("/authors/"+str(new_author.id))

def index2(request):
    context = {
        "all_the_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/index2.html", context)


def author(request, my_val):
    context = {
        "Author": Author.objects.get(id=my_val),
        "Books": Author.objects.get(id=my_val).books,
        "allbook": Book.objects.all(),
    }
    return render(request, "books_authors_app/authors.html", context)

def addbooktoauthor(request):
    if request.method == "POST":
        id = request.POST["authors"]
        author = Author.objects.get(id=id)
        book_id = request.POST["bookid"]
        books = Book.objects.get(id=book_id)
        author.books.add(books)

        return redirect('/author/' + id)


def addnewauthor(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        notes = request.POST["notes"]
        new_author = Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)

        return redirect('/author/' + str(new_author.id))