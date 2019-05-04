"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',testapp.views.PostList.as_view(),name="home"),
    path('start',testapp.views.start,name="start"),
    # 아래 부터 CRUD 4가지 
    # 영화를 생성할 url (Create)
    path('create/',testapp.views.PostCreate.as_view(),name="create"),
    # 각 영화 detail url(Read)
    path('detail/<int:pk>',testapp.views.PostDetail.as_view(),name="detail"),
    # 영화를 수정할 url (Update)
    path('update/<int:pk>',testapp.views.PostUpdate.as_view(),name="update"),
    # 영화를 제거할 url (Delete)
    path('delete/<int:pk>',testapp.views.PostDelete.as_view(),name="delete"),
]