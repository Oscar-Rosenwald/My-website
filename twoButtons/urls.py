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
    path('blog/new/', views.post_new, name="new_post"),
    path('blog/<int:pk>/edit/', views.post_edit, name="edit_post"),
]
