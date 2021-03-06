from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import SyllableWord


class SyllableWordIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'syllablewords.view_syllableword'
    template_name = "syllablewords/index.html"
    model = SyllableWord
    context_object_name = 'words'
    queryset = SyllableWord.objects.filter(orig_num=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class SyllableWordBookListView(PermissionRequiredMixin, ListView):
    permission_required = 'syllablewords.view_syllableword'
    template_name = "syllablewords/booklist.html"
    model = SyllableWord
    context_object_name = 'words'

    def get_queryset(self, *args, **kwargs):
        return SyllableWord.objects.filter(orig_book=self.kwargs.get('orig_book'))\
            .filter(orig_box=self.kwargs.get('orig_box'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class SyllableWordDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'syllablewords.view_syllableword'
    template_name = "syllablewords/detailview.html"
    context_object_name = 'words'

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(SyllableWord, id=_id)

    def get_context_data(self, **kwargs):
        # super() = Function used to give access to the methods of a parent class.
        # Returns a temporary object of a parent class when used
        context = super().get_context_data(**kwargs)
        try:
            context['prev_url'] = SyllableWord.objects.get(id=int(self.kwargs.get("id")) - 1)
        except ObjectDoesNotExist:
            context['prev_url'] = None

        try:
            context['next_url'] = SyllableWord.objects.get(id=int(self.kwargs.get("id")) + 1)
        except ObjectDoesNotExist:
            context['next_url'] = None

        context['ref_tab'] = True
        return context
