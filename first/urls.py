from django.contrib import admin
from django.urls import path
from .views import postAPI, listpostAPI

urlpatterns = [

    path("post/", postAPI.as_view(), name='post_create'),
    path('listpost/', listpostAPI),

]
