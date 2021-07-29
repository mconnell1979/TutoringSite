from django.shortcuts import render
from django.views.generic.base import TemplateView


def empty(request):
    # return HttpResponse('Sight Words Index')
    return render(request, 'pages/empty.html')


class IndexView(TemplateView):
    template_name = "pages/home_page.html"

    def get_context_data(self, *args, **kwargs):
        return None
