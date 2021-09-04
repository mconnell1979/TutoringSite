from django.urls import path
from . import views


app_name = 'hackablesheets'
urlpatterns = [
    path('', views.HackableBookIndexView.as_view(), name='BookIndex'),
    path('WordSheetList/<int:orig_book>', views.HackableWordSheetIndexView.as_view(),
         name='SheetIndex'),
    path('WordSheet/<int:pk>', views.HackableWordSheetDetailView.as_view(),
         name='Sheet'),
    path('Word/<int:pk>/<int:wordnum>/<str:hackword>', views.HackableWordDetailView.as_view(),
         name='HackableWord'),
    path('SentenceSheetList/<int:orig_book>', views.HackableSentenceSheetIndexView.as_view(),
         name='SentenceSheetIndex'),
    path('SentenceSheet/<int:pk>', views.HackableSentenceSheetDetailView.as_view(),
         name='HackableSentenceSheet'),
    path('Sentence/<int:pk>/<int:sentencenum>/<str:sentence>', views.HackableSentenceDetailView.as_view(),
         name='HackableSentence'),
]