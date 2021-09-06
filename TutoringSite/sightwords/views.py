from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import SightWord, SightWordSentences


class SightWordIndexView(PermissionRequiredMixin, ListView):
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


class SightWordDetailView(PermissionRequiredMixin, DetailView):
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


class SightWordSentenceIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'sightwords.view_sightwordsentences'
    template_name = "sightwords/sentences/sentence_index.html"
    model = SightWordSentences
    context_object_name = 'sentences_obj'
    queryset = SightWordSentences.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['sight_word_list'] = self.model.objects.get(pk=self.kwargs.get('pk'))
        context['ref_tab'] = True
        return context


class SightWordSentenceView(PermissionRequiredMixin, DetailView):
    permission_required = 'sightwords.view_sightwordsentences'
    template_name = "sightwords/sentences/sentences_and_words.html"
    context_object_name = 'obj_sentence'
    model = SightWordSentences

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sight_words'] = self.object.sight_word.all()
        context['ref_tab'] = True
        return context


class WordCardView(PermissionRequiredMixin, ListView):
    permission_required = 'sightwords.view_sightwordsentences'
    template_name = "sightwords/cardview.html"
    model = SightWordSentences
    paginate_by = 1
    context_object_name = 'words'
    # page_obj = Paginator.page(number=3)

    def get_queryset(self):
        sentenceobj = self.model.objects.get(pk=self.kwargs.get('pk'))
        myquery = sentenceobj.sight_word.all()
        return myquery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myobj'] = self.model.objects.get(pk=self.kwargs.get('pk'))
        context['ref_tab'] = True
        return context
