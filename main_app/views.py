from django.shortcuts import render
from django.db import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ItemCreate(request):
    return render(request, 'create.html')

# class ItemList(ListView): 
#     model = Item

# class ItemDelete(DeleteView):
#     model = Item
#     def get_success_url(self):
#         return reverse('', args=[self.object.item.id])