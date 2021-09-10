from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import SRABook, SRAPassage


class SRAPassageIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'SRABook.view_SRABook'
    template_name = "read_in_context/index.html"
    model = SRAPassage
    context_object_name = 'SRAPassages'
    queryset = SRAPassage.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class SRAPassageDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'SRABook.view_SRABook'
    template_name = "read_in_context/SRAPassagedetail.html"
    model = SRAPassage
    context_object_name = 'SRAPassage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context