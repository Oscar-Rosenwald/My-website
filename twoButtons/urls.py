"""twoButtons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from django.conf.urls import include
from django.urls import path
from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.two_buttons, name="home"),
    url('cv', views.cv_view, name="CV"),
    path('blog', views.blog_view, name="blogs"),
    path('blog/<int:pk>/', views.post_view, name="posts"),

    # New
    path('blog/new/', views.post_new, name="new_post"),
    path('education/new/', views.education_new, name="new_education"),
    path('reference/new/', views.reference_new, name="new_reference"),
    path('personal-interest/new/', views.personal_interests_new, name="new_personal_interest"),
    path('project/new', views.project_new, name='new_project'),
    path('work-experience/new', views.work_experience_new, name="new_work_experience"),
    path('technical-skill/new', views.tech_skill_new, name="new_tech_skill"),
    path('others/new', views.others_new, name='new_others'),

    # Edits
    path('blog/<int:pk>/edit/', views.post_edit, name="edit_post"),
    path('education/<int:pk>/edit', views.education_edit, name="edit_education"),
    path('reference/<int:pk>/edit', views.reference_edit, name='edit_reference'),
    path('personal-interest/<int:pk>/edit/', views.personal_interests_edit, name='edit_personal_interest'),
    path('project/<int:pk>/edit/', views.project_edit, name='edit_project'),
    path('work-experience/<int:pk>/edit', views.work_experience_edit, name='edit_work_experience'),
    path('technical-skill/<int:pk>/edit', views.tech_skill_edit, name="edit_tech_skill"),
    path('others/<int:pk>/edit', views.others_edit, name="edit_others"),

    # # Edits of Personal Info
    path('person/edit', views.person_edit, name='edit_person'),
]
