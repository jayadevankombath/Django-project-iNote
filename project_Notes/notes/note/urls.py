"""notes URL Configuration

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
from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'home/$',views.user_home,name="userhome"),
    url(r'valid/$',views.Validfrm.as_view(),name="newaccount"),
    url(r'log/$',views.log,name="login"),
    url(r'logout/$',views.logout,name="logout"),
    url(r'addnote/(?P<id>\d+)$',views.add_note,name="addnoteuser"),
    url(r'editnote/(?P<id>\d+)$',views.edit_note,name="editnote"),
    url(r'savenote/(?P<id>\d+)$',views.save_note,name="savenote"),
    url(r'delnote/(?P<id>\d+)$',views.del_note,name="delnote")

]