from django.urls import path
from .views import IndexView
from .views import ContactView
from .views import WorkWithUsView
from . import views

app_name = 'pages'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('workwithus/', WorkWithUsView.as_view(), name='workwithus'),
    path('empty', views.empty),
    ]