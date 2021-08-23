from django.urls import path
from . import views

# app_name:name is what is used for the url ref
app_name = 'lessonplans'
urlpatterns = [
    path('', views.LessonIndexView.as_view(), name='Index'),
    path('tutor/', views.LessonTutorIndexView.as_view(), name='LessonPlanTutorIndex'),
    # path('create/', views.lessonplan_create_function),
    path('create/', views.LessonplanCreateView.as_view(), name='LessonPlanCreate'),
    path('<int:pk>/update/', views.LessonplanUpdateView.as_view(), name='Update'),
    path('<int:pk>/', views.LessonplanDetailView.as_view(), name='detail'),
    path('<int:pk>/<str:wordtype>/word_card/', views.WordCardView.as_view(), name='card'),
    path('<int:lesson_id>/sight_words/<int:pk>/', views.PersonalSightWordCardView.as_view(), name='sight_words'),
    path('<int:lesson_id>/hack_words/<int:pk>/', views.LessonplanHackSetDetailView.as_view(), name='hack_words'),
    path('<int:lesson_id>/hack_words/<int:pk>/<int:wordnum>/<str:hackword>',
         views.LessonplanHackWordDetailView.as_view(), name='hackable_word'),
    path('<int:lesson_id>/hack_sent_set/<int:pk>/', views.LessonplanHackSentSetDetailView.as_view(), name='hacksent_set'),
    path('<int:lesson_id>/hack_sent/<int:pk>/<int:sentencenum>/<str:sentence>',
         views.LessonplanHackSentDetailView.as_view(), name='hackable_sent'),
    path('<int:lesson_id>/hack_sent_word/<int:pk>/<int:wordnum>/<str:word>',
         views.LessonplanHackSentWordDetailView.as_view(), name='hackable_sent_word'),
    path('grade', views.update_grade),
]
