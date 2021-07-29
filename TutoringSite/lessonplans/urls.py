from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listview', views.LessonplanListView.as_view()),
    path('createview', views.LessonplanCreateView.as_view()),
    path('lessonview', views.LessonView.as_view()),
    path('create/', views.lesson_plan_create_view),
    path('<int:id>/', views.LessonplanDetailView.as_view()),
    path('grade', views.update_grade),
]