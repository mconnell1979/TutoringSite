from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import VVStoryBook, VVStory, VVStoryQuestion


class VVStoryBookIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'vv_stories.view_vv_stories'
    template_name = "vv_stories/index.html"
    model = VVStoryBook
    context_object_name = 'books'
    queryset = VVStoryBook.objects.all()
    # print("vv_stories List View Book Trying")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class VVStoryIndexView(PermissionRequiredMixin, ListView):
    permission_required = 'vv_stories.view_vv_stories'
    template_name = "vv_stories/storyindex.html"
    model = VVStory
    context_object_name = 'stories'

    def get_queryset(self, *args, **kwargs):
        print("Ok: Let's See...")
        print(self.kwargs.get("book"))
        print(VVStory.objects.filter(book_id=self.kwargs.get("book")))
        return VVStory.objects.filter(book_id=self.kwargs.get('book'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ref_tab'] = True
        return context


class StoryDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'vvstory.view_vv_stories'
    template_name = "vv_stories/storydetail.html"
    context_object_name = 'story'
    model = VVStory
    print("hmm...")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Note: personalizing the context data allows you to get more organized context and other object data.? \()/
        context['questions'] = VVStoryQuestion.objects.filter(story=self.kwargs.get("pk"))
        # Connor had the line below. I thought iy worked but it doesn't.  How would you ref this?
        # context['sentences'] = str(context['story']).split(".")
        context['sentences'] = str(self.object.story).split(".")
        print("Story Detail View Executing...")
        print(context['questions'])
        print(context['story'])
        context['ref_tab'] = True
        return context
