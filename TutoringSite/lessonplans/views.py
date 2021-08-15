from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from lessonplans.models import LessonPlan, PersonalSightWord
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from lessonplans.forms import LessonPlanForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LessonIndexView(LoginRequiredMixin, ListView):
    template_name = "lessonplans/index.html"
    login_url = '/login/'
    model = LessonPlan
    context_object_name = 'lessons'

    def get_queryset(self):
        return self.model.objects.filter(tutor=self.request.user)

    def get_context_data(self, **kwargs):
        # using super() calls the parent function just like it would anyway
        # if you don't use it then you're completely overriding the function.
        context = super().get_context_data(**kwargs)
        context['lessonplan_tab'] = True
        return context


class LessonplanDetailView(PermissionRequiredMixin, DetailView):
    template_name = "lessonplans/lessonplan_detail.html"
    context_object_name = 'lesson'
    model = LessonPlan
    login_url = '/login/'
    permission_required = ('lessonplans.add_lessonplan', 'lessonplans.view_lessonplan')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Note: personalizing the context data allows you to get more organized context and other object data.? \()/
        context['sight_word_list'] = self.object.sight_word_list.all()
        context['syllable_word_list'] = self.object.syllable_word_list.all()
        context['multisyllable_word_list'] = self.object.multisyllable_word_list.all()
        context['affix_word_list'] = self.object.affix_word_list.all()
        context['personal_word_list'] = PersonalSightWord.objects.filter(student=self.object.student.id)
        context['hackable_word_set_list'] = self.object.hackable_word_set_list.all()
        context['hackable_sentence_set_list'] = self.object.hackable_sentence_set_list.all()
        context['lessonplan_tab'] = True
        return context


class WordCardView(LoginRequiredMixin, ListView):
    template_name = "lessonplans/cardview.html"
    login_url = '/login/'
    model = LessonPlan
    paginate_by = 1
    context_object_name = 'words'

    def get_queryset(self):
        print('wordtype: ' + self.kwargs.get('wordtype'))
        lessonobj = self.model.objects.get(pk=self.kwargs.get('pk'))
        if self.kwargs.get('wordtype') == 'capture':
            myquery = lessonobj.sight_word_list.all()
        elif self.kwargs.get('wordtype') == 'syllable':
            myquery = lessonobj.syllable_word_list.all()
        elif self.kwargs.get('wordtype') == 'multisyllable':
            myquery = lessonobj.multisyllable_word_list.all()
        elif self.kwargs.get('wordtype') == 'affix':
            myquery = lessonobj.affix_word_list.all()
        else:
            myquery = 'configure your href'
        return myquery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myobj'] = self.model.objects.get(pk=self.kwargs.get('pk'))
        context['lessonplan_tab'] = True
        return context


class PersonalSightWordCardView(LoginRequiredMixin, ListView):
    template_name = "lessonplans/personalsightcardview.html"
    login_url = '/login/'
    model = PersonalSightWord
    paginate_by = 1
    context_object_name = 'words'

    def get_queryset(self):
        personal_words_obj = self.model.objects.get(pk=self.kwargs.get('pk'))
        my_query = self.model.objects.filter(student=personal_words_obj.student.id)
        return my_query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessonid'] = self.kwargs.get("lesson_id")
        context['myobj'] = self.model.objects.get(pk=self.kwargs.get('pk'))
        context['lessonplan_tab'] = True
        return context


class LessonplanHackWordDetailView(LoginRequiredMixin, DetailView):
    template_name = "lessonplans/hackword_detail.html"
    context_object_name = 'sheet'
    model = LessonPlan
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.object.hackable_word_set_list.all())
        context['hackable_word_set_list'] = self.object.hackable_word_set_list.all()
        context['lessonplan_tab'] = True
        return context


def lessonplan_create_function(request):
    form = LessonPlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form.LessonPlanForm()  # This Re-renders the form after the save and will blank or default all the fields out.

    context = {
        'form': form
    }
    return render(request, "lessonplans/lessonplan_create.html", context)


# My First Class Based Template View
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "lessonplans/lesson_plan.html"
    login_url = '/admin/login/'

    def get_context_data(self, **kwargs):
        # super() = Function used to give access to the methods of a parent class.
        # Returns a temporary object of a parent class when used
        context = super().get_context_data(**kwargs)
        context['lessons'] = LessonPlan.objects.all()
        print('!==== get context data just called, yep ====!')
        print(context)
        return context

    def stupid_method(self, **kwargs):
        # This is just for learning
        # This first line basically sets context to something like:
        # {'view': <lessonplans.views.IndexView object at 0x00000203D45C8C10>}
        context = super().get_context_data(**kwargs)
        print("context - printed")
        print(str(context))
        # This second line keys this data with lessons and stores all the db objects as values for this key.
        context['lessons'] = LessonPlan.objects.all()
        print("context - printed again after: context[lessons] is set")
        print(str(context))
        print("")
        print("The return comes next:")
        return context['lessons']


@csrf_exempt
def update_grade(request):
    if request.method =="POST":
        return JsonResponse({'foo': 'bar'})
    else:
        return JsonResponse({"error": "Expected POST"})

