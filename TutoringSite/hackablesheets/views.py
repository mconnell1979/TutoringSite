from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import HackableWordSet, HackableBook


class HackableBookIndexView(LoginRequiredMixin, ListView):
    template_name = "hackablesheets/index.html"
    model = HackableBook
    context_object_name = 'books'
    queryset = HackableBook.objects.all()
    login_url = '/login/'


class HackableWordSetIndexView(LoginRequiredMixin, ListView):
    template_name = "hackablesheets/index.html"
    model = HackableWordSet
    context_object_name = 'sheets'
    queryset = HackableWordSet.objects.filter(orig_num=1)
    login_url = '/login/'
