from django.shortcuts import render
from django.views.generic.base import TemplateView


def empty(request):
    # return HttpResponse('Sight Words Index')
    return render(request, 'pages/empty.html')


class IndexView(TemplateView):
    template_name = "pages/home_page.html"

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['home_tab'] = True
        return context


class ContactView(TemplateView):
    template_name = "pages/contact_us.html"

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['contact_tab'] = True
        return context


class WorkWithUsView(TemplateView):
    template_name = "pages/work_with_us.html"

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['workwithus_tab'] = True
        return context