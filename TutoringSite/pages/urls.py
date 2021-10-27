from django.urls import path
from .views import IndexView
from .views import ContactView
from . import views

app_name = 'pages'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('empty', views.empty),
    ]