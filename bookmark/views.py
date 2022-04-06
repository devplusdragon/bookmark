from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from bookmark.models import Bookmark
from django.urls import reverse_lazy


# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class BookmarkDetail(DetailView):
    model = Bookmark


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
