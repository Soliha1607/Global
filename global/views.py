from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from .models import Work, About, Contact

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['works'] = Work.objects.all()
        print("===============================")
        print(context['works'])
        context['abouts'] = About.objects.all()
        print("===============================")
        print(context['abouts'])
        context['contacts'] = Contact.objects.all()
        print("===============================")
        print(context['contacts'])
        return context