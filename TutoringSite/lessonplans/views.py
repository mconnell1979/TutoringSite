from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from lessonplans.models import LessonPlan
from sightwords.models import SightWord
from syllablewords.models import SyllableWord
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from lessonplans.forms import LessonPlanForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LessonIndexView(LoginRequiredMixin, ListView):
    template_name = "lessonplans/index.html"
    login_url = '/login/'
    model = LessonPlan
    context_object_name = 'lessons'

    def get_queryset(self, *args, **kwargs):
        print('wtf1')
        print(self.request.user)
        # return LessonPlan.objects.all()
        print(LessonPlan.objects.filter(tutor=self.request.user))
        return LessonPlan.objects.filter(tutor=self.request.user)

class LessonplanListView(ListView):
    # template_name = "lessonplans/lesson_plan_listview.html"
    # This Listview class defaults to model_list.html unless you override the template_name attribute.
    model = LessonPlan
    context_object_name = 'lesson'
    print(model.student)


class LessonplanDetailView(PermissionRequiredMixin, DetailView):
    template_name = "lessonplans/lessonplan_detailview.html"
    context_object_name = 'lesson'
    login_url = '/login/'
    permission_required = ('lessonplans.add_lessonplan', 'lessonplans.view_lessonplan')

    def get_object(self, **kwargs):
        _id = self.kwargs.get("id")
        return get_object_or_404(LessonPlan, id=_id)

    def get_context_data(self, **kwargs):
        # super() = Function used to give access to the methods of a parent class.
        # Returns a temporary object of a parent class when used
        context = super().get_context_data(**kwargs)

        # context['lesson'] = LessonPlan.objects.get(id=self.kwargs.get("id"))
        # context['sight_word_list'] = self.object.sight_word_list.all()
        context['sight_word_list'] = self.object.sight_word_list.all()
        context['sightwords'] = \
            SightWord.objects.all().filter(order__gte=context['lesson'].sight_words_start)\
                                   .filter(order__lte=context['lesson'].sight_words_end)
        context['syllablewords'] = \
            SyllableWord.objects.all().filter(order__gte=context['lesson'].syllable_words_start)\
                                      .filter(order__lte=context['lesson'].syllable_words_end)
        return context


class LessonplanCreateView(CreateView):
    model = LessonPlan
    template_name = "lessonplans/lessonplan_createview.html"
    context_object_name = 'lesson_plan'


class LessonView(LoginRequiredMixin, TemplateView):
    template_name = "lessonplans/carousel.html"
    login_url = '/admin/login/'

    def get_context_data(self, **kwargs):
        # super() = Function used to give access to the methods of a parent class.
        # Returns a temporary object of a parent class when used
        context = super().get_context_data(**kwargs)
        context['lessons'] = LessonPlan.objects.all()
        context['sightwords'] = SightWord.objects.all().filter(order__gte=300).filter(order__lte=310)
        context['syllablewords'] = SyllableWord.objects.all().filter(order__gte=400).filter(order__lte=410)
        print('!==== Lesson View get context data just called huh? ====!')
        print('all context::::---->')
        print(context)
        print('sigthwords::::---->')
        #print(context['sightwords'])
        print('syllablewords::::---->')
        #print(context['syllablewords'])
        return context


# def lesson_plan_create_view(request):
#     my_form = RawLessonPlanForm(request.POST)
#     context = {
#         'form': my_form
#     }
#     return render(request, "lessonplans/lesson_plan_create.html", context)


def lesson_plan_create_view(request):
    form = LessonPlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form.LessonPlanForm()  # This Re-renders the form after the save and will blank or default all the fields out.

    context = {
        'form': form
    }
    return render(request, "lessonplans/lesson_plan_create.html", context)

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
