from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book


def home(request):
    books = Book.objects.all()
    return render(request, "mainapp/home.html", {"books": books})


def about(request):
    return render(request, "mainapp/about.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required(login_url="/login/")
def profile(request):
    books = Book.objects.all()
    return render(request, "mainapp/profile.html", {"books": books})


@login_required(login_url="/login/")
def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            category=request.POST.get("category"),
            description=request.POST.get("description"),
            image=request.POST.get("image"),
        )
        return redirect("profile")

    return render(request, "mainapp/add_book.html")


@login_required(login_url="/login/")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("profile")

    return render(request, "mainapp/delete_book.html", {"book": book})


def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="/login/")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.category = request.POST.get("category")
        book.description = request.POST.get("description")
        book.image = request.POST.get("image")
        book.save()
        return redirect("profile")

    return render(request, "mainapp/edit_book.html", {"book": book})
