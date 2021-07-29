from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import SyllableWord


def index(request):
    # return HttpResponse('Sight Words Index')
    return render(request, 'syllablewords/index.html')


def wordlist(request):
    words = SyllableWord.objects.all()
    return render(request, 'syllablewords/wordlist.html',
                  {'words': words})


class CarouselView(TemplateView):
    None


# def carousellist(request):
#     # words = SightWord.objects.filter(name__exact='is')
#     x = 11-1
#     y = 20
#     words = SyllableWord.objects.all()[x:y]
#     return render(request, 'syllablewords/carousel.html', {'words': words})