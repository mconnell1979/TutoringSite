from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import HackableWordSet, HackableBook, HackableSentenceSet


class HackableBookIndexView(LoginRequiredMixin, ListView):
    template_name = "hackablesheets/index.html"
    model = HackableBook
    context_object_name = 'books'
    queryset = HackableBook.objects.all()
    login_url = '/login/'


class HackableWordSheetIndexView(LoginRequiredMixin, ListView):
    template_name = "hackablesheets/wordsheetindex.html"
    login_url = '/login/'
    model = HackableWordSet
    context_object_name = 'sheets'

    def get_queryset(self, *args, **kwargs):
        return HackableWordSet.objects.filter(book__orig_book=self.kwargs.get('orig_book'))


class HackableWordSheetDetailView(LoginRequiredMixin, DetailView):
    template_name = "hackablesheets/wordsetdetail.html"
    context_object_name = 'sheet'
    login_url = '/login/'

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(HackableWordSet, id=_id)


class HackableWordDetailView(LoginRequiredMixin, DetailView):
    template_name = "hackablesheets/worddetail.html"
    context_object_name = 'sheet'
    login_url = '/login/'

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(HackableWordSet, id=_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wordnum'] = self.kwargs.get("wordnum")
        context['hackword'] = self.kwargs.get("hackword")
        return context


class HackableSentenceSheetIndexView(LoginRequiredMixin, ListView):
    template_name = "hackablesheets/sentencesheetindex.html"
    login_url = '/login/'
    model = HackableSentenceSet
    context_object_name = 'sheets'

    def get_queryset(self, *args, **kwargs):
        return HackableSentenceSet.objects.filter(book__orig_book=self.kwargs.get('orig_book'))


class HackableSentenceSheetDetailView(LoginRequiredMixin, DetailView):
    template_name = "hackablesheets/sentencesetdetail.html"
    context_object_name = 'sheet'
    login_url = '/login/'

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(HackableSentenceSet, id=_id)


class HackableSentenceDetailView(LoginRequiredMixin, DetailView):
    template_name = "hackablesheets/sentencedetail.html"
    context_object_name = 'sheet'
    login_url = '/login/'

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(HackableWordSet, id=_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sentencenum'] = self.kwargs.get("sentencenum")
        context['sentence'] = self.kwargs.get("sentence")
        return context
