from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Work, About, Contact

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['work'] = Work.objects.all()
        print("===============================")
        print(context['work'])
        context['about'] = About.objects.all()
        print("===============================")
        print(context['about'])
        context['contact'] = Contact.objects.all()
        print("===============================")
        print(context['contact'])
        return context
