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
    path('',testapp.views.index,name="index"),
    path('create/',testapp.views.create,name="create"),
    path('detail/<int:pk>',testapp.views.detail,name="detail"),
    path('update/<int:pk>',testapp.views.update,name="update"),
    path('delete/<int:pk>',testapp.views.delete,name="delete"),
    path('participate/<int:pk>',testapp.views.participate, name="participate"),
    path('unparticipate/<int:pk>',testapp.views.unparticipate,name="unparticipate"),
    path('reserve',testapp.views.reserve,name="reserve"),
    path('reserve_house',testapp.views.reserve_house,name="reserve_house"),
    path('reserve_finish',testapp.views.reserve_finish,name="reserve_finish"),
]
