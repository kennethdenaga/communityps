from django.conf.urls import url, include
from django.contrib import admin
from kenlist import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^kenlist/new$', views.new_donator, name='new_donator'),    
    url(r'^kenlist/(\d+)/$', views.view_donator, name='view_donator'),    
    url(r'^kenlist/(\d+)/add_donation$', views.add_donation, name='add_donation'),]
    

