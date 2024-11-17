from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='homeblog'),
    # path('base',base,name='base'),
    path('cbvlist',tasklistview.as_view(),name='listblog'),
    path('cbvdetail/<int:pk>/',taskDetailstview.as_view(),name='view_details'),
    path('cbvcreate',PostCreateView.as_view(),name='create_post'),
    path('cbvupdate/<int:pk>/',TaskUpdateView.as_view(),name='view_update'),
    path('cbvdelete/<int:pk>/',TaskDeleteView.as_view(),name='view_Delete'),
    path('usercreation/',usercreation,name='usercreation')
    
]