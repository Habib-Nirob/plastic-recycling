from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('Blogs',views.Blogs,name='Blogs'),
    path('Contact',views.Contact,name='Contact'),
    path('offset',views.offset,name='offset'),
    path('forbands',views.forbands,name='forbands'),
    path('signup',views.signup,name='signup'),
    
]