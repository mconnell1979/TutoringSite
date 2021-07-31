from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import SightWord


class SightwordIndexView(ListView):
    template_name = "sightwords/index.html"
    model = SightWord
    context_object_name = 'words'
    queryset = SightWord.objects.filter(orig_num=1)


class SightwordSetListView(ListView):
    template_name = "sightwords/setlist.html"
    model = SightWord
    context_object_name = 'words'

    def get_queryset(self, *args, **kwargs):
        return SightWord.objects.filter(orig_set=self.kwargs.get('orig_set'))


class SightwordDetailView(LoginRequiredMixin, DetailView):
    template_name = "sightwords/detailview.html"
    context_object_name = 'words'
    login_url = '/login/'

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(SightWord, id=_id)

    def get_context_data(self, **kwargs):
        # super() = Function used to give access to the methods of a parent class.
        # Returns a temporary object of a parent class when used
        context = super().get_context_data(**kwargs)
        try:
            context['prev_url'] = SightWord.objects.get(id=int(self.kwargs.get("id")) - 1)
        except ObjectDoesNotExist:
            context['prev_url'] = None

        try:
            context['next_url'] = SightWord.objects.get(id=int(self.kwargs.get("id")) + 1)
        except ObjectDoesNotExist:
            context['next_url'] = None

        return context


# Delete All These Function Based Views Below
# def index(request):
#     #  return HttpResponse('Sight Words Index')
#     return render(request, 'sightwords/index.html')
#
#
# def wordlist(request):
#     words = SightWord.objects.all()
#     return render(request, 'sightwords/wordlist.html', {'words': words})


def carousellist(request):
    # words = SightWord.objects.filter(name__exact='is')
    # words = SightWord.objects.filter(name__endswith='ed')
    # words = SightWord.objects.all()[21:36]
    words = SightWord.objects.filter(order__gte=300).filter(order__lte=310)
    print('test ======================')
    print(words)
    paginator = Paginator(words, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sightwords/carousel.html',
                  {'page_obj': page_obj})
