"""tutoringsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#imports for images:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('sightwords/', include('sightwords.urls')),
    path('syllablewords/', include('syllablewords.urls')),
    path('hackablesheets/', include('hackablesheets.urls')),
    path('lessonplans/', include('lessonplans.urls')),
    path('read_in_context/', include('read_in_context.urls')),
    path('vv_stories/', include('vv_stories.urls')),
    path('vv_pictures/', include('vv_pictures.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
