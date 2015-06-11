from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Part



class PartListView(ListView):
    model = Part
    context_object_name="part_list"
    queryset = Part.objects.all().order_by('id')


    def get_context_data(self, **kwargs):
        context = super(PartListView, self).get_context_data(**kwargs)
        return context

class PartDetailView(DetailView):
    context_object_name = "partpic"
    model = Part