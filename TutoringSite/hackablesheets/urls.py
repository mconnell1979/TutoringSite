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
    # path('WordSetIndex/<int:orig_set>', views.HackableWordSetIndexView.as_view(), name='HackableWordSetIndex'),
    # path('SightWordSetList/<int:orig_set>', views.HackableWordSetIndexView.as_view(), name='HackableWordSetIndex'),
    # path('<int:id>/', views.SightwordDetailView.as_view(), name='Detail'),
]