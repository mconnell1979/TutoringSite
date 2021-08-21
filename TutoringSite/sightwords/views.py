from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import SightWord


class SightwordIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'sightwords.view_sightword'
    template_name = "sightwords/index.html"
    model = SightWord
    context_object_name = 'words'
    queryset = SightWord.objects.filter(orig_num=1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class SightWordSetListView(PermissionRequiredMixin, ListView):
    permission_required = 'sightwords.view_sightword'
    template_name = "sightwords/setlist.html"
    model = SightWord
    context_object_name = 'words'


    def get_queryset(self, *args, **kwargs):
        return SightWord.objects.filter(orig_set=self.kwargs.get('orig_set'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class SightwordDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'sightwords.view_sightword'
    template_name = "sightwords/detailview.html"
    context_object_name = 'words'

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

        context['ref_tab'] = True
        return context

