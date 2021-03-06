from django.conf.urls import url, include
from django.contrib import admin
from kenlist import views 

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^kenlist/new$', views.new_donator, name='new_donator'),    
    url(r'^kenlist/(\d+)/$', views.view_donator, name='view_donator'),    
    url(r'^kenlist/(\d+)/add_donation$', views.add_donation, name='add_donation'),
    url(r'^kenlist/homepage$', views.homepage, name='homepage'),
    url(r'^kenlist/donator$', views.donator, name='donator'),
    url(r'^kenlist/donation$', views.donation, name='donation'),
    url(r'^kenlist/recepient$', views.recepient, name='recepient'),
    url(r'^kenlist/location$', views.location, name='location'),
    url(r'^kenlist/remarks$', views.remarks, name='remarks'),
    url(r'^kenlist/profile$', views.profile, name='profile'),
    url(r'^kenlist/about$', views.about, name='about'),
    url(r'^kenlist/info$', views.info, name='info'),
    url(r'^kenlist/contact$', views.contact, name='contact'),
    ]
    

