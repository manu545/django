from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView

from .import views
# Add this import
admin.autodiscover()

urlpatterns = (
     url(r'^profile/$', TemplateView.as_view(template_name='userprof.html')),
     url(r'^profileupdated/$', TemplateView.as_view(template_name='profileupdated.html')),
     url(r'^updateprofile/$', views.update_profile, name='update_profile'),
     url(r'new/$', views.Register.as_view(), name='reg-new'),
     url(r'^search/$', views.search, name= 'search'),

    #     url(r'^profile/(?P<profile_id>[\d]+)/$', TemplateView.as_view(template_name='userprof.html')),

)