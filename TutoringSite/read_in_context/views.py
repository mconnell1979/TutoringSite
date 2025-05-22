from django.views.generic import ListView, DetailView
from .models import SRABook, SRAPassage
from django.contrib.auth.mixins import PermissionRequiredMixin

# existing index view
class SRAPassageIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'SRABook.view_SRABook'
    template_name = "read_in_context/index.html"
    model = SRAPassage
    context_object_name = 'SRAPassages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context

# 👇 new detail view for individual passage
class SRAPassageDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'SRABook.view_SRABook'
    template_name = "read_in_context/SRAPassagedetail.html"
    model = SRAPassage
    context_object_name = 'SRAPassage'
