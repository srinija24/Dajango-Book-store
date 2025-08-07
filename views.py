from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book


class BooksListView(ListView):
    model=Book
    template_name='list.html'

class BookDetailView(DetailView):
    model=Book
    template_name='detail.html'

class BookCheckoutView(DetailView):
    model=Book
    template_name='checkout.html'