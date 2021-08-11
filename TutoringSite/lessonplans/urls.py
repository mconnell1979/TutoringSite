from django.urls import path
from . import views

app_name = 'lessonplans'
urlpatterns = [
    path('', views.LessonIndexView.as_view(), name='LessonPlanIndex'),
    path('listview', views.LessonplanListView.as_view(), name='listview'),
    path('createview', views.LessonplanCreateView.as_view(), name='create'),
    path('lessonview', views.LessonView.as_view()),
    path('create/', views.lesson_plan_create_view),
    path('<int:id>/', views.LessonplanDetailView.as_view(), name='detail'),
    path('grade', views.update_grade),
]