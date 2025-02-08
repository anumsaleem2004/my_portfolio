"""
URL configuration for djangoProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('anum/',views.add_skills, name='skills'),
    path('delete-skills/', views.delete_skills, name='delete_skills'),
    path('delete-projects/', views.delete_projects, name='delete_projects'),
    path('delete-education/', views.delete_education, name='delete_education'),
    path('delete-experience/', views.delete_experience, name='delete_experience'),
    path('delete-certifications/', views.delete_certifications, name='delete_certifications'),
    path('delete-tools/', views.delete_tools, name='delete_tools'),

   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






