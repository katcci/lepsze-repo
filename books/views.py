from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# http://127.0.0.1:8000/
from books.models import Book

def stronka(request):
    print(request.user.is_authenticated)
    return render(request, "stronka.html")

def books_list(request):
    context = {"books": Book.objects.all()}
    return render(request, "book_list.html", context)
#class IndexView(TemplateView):
    #template_name = "index.html"   