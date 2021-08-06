from django.urls import path
from . import views


app_name = 'hackablesheets'
urlpatterns = [
    path('', views.HackableBookIndexView.as_view(), name='HackableBookIndex'),
    path('WordSheetList/<int:orig_book>', views.HackableWordSheetIndexView.as_view(),
         name='HackableWordSheetIndex'),
    path('WordSheet/<int:id>', views.HackableWordSheetDetailView.as_view(),
         name='HackableWordSheet'),
    path('Word/<int:id>/<int:wordnum>/<str:hackword>', views.HackableWordDetailView.as_view(),
         name='HackableWord'),
    path('SentenceSheetList/<int:orig_book>', views.HackableSentenceSheetIndexView.as_view(),
         name='HackableSentenceSheetIndex'),
    path('SentenceSheet/<int:id>', views.HackableSentenceSheetDetailView.as_view(),
         name='HackableSentenceSheet'),
]