from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.shortcuts import get_object_or_404
from .models import HackableWordSet, HackableBook, HackableSentenceSet


class HackableBookIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/index.html"
    model = HackableBook
    context_object_name = 'books'
    queryset = HackableBook.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class HackableWordSheetIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/wordset/wordsheetindex.html"
    model = HackableWordSet
    context_object_name = 'sheets'

    def get_queryset(self, *args, **kwargs):
        return HackableWordSet.objects.filter(book__orig_book=self.kwargs.get('orig_book'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class HackableWordSheetDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/wordset/wordsetdetail.html"
    context_object_name = 'sheet'
    model = HackableWordSet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class HackableWordDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/wordset/worddetail.html"
    context_object_name = 'sheet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wordnum'] = self.kwargs.get("wordnum")
        context['hackword'] = self.kwargs.get("hackword")
        context['ref_tab'] = True
        return context


class HackableSentenceSheetIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/sentences/sentencesheetindex.html"
    model = HackableSentenceSet
    context_object_name = 'sheets'

    def get_queryset(self, *args, **kwargs):
        return HackableSentenceSet.objects.filter(book__orig_book=self.kwargs.get('orig_book'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class HackableSentenceSheetDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/sentences/sentencesetdetail.html"
    model = HackableSentenceSet
    context_object_name = 'sheet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class HackableSentenceDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'hackablesheets.view_hackablebook'
    template_name = "hackablesheets/sentences/sentencedetail.html"
    model = HackableSentenceSet
    context_object_name = 'sheet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sentencenum'] = self.kwargs.get("sentencenum")
        context['sentence'] = self.kwargs.get("sentence")
        context['ref_tab'] = True
        return context
