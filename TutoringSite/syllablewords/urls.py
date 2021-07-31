from django.urls import path
from . import views

app_name='syllablewords'
urlpatterns = [
    path('', views.SyllableWordIndexView.as_view(), name='SyllableWordsIndex'),
    path('SyllableWordBookList/<int:orig_box>/<int:orig_book>', views.SyllableWordBookListView.as_view(), name='BookList'),
    path('<int:id>/', views.SyllableWordDetailView.as_view(), name='Detail'),
]