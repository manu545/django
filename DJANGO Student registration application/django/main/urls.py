from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from starboy.forms import LoginForm



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('starboy.urls')),
    url(r'^login/$', views.LoginView.as_view(), {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), {'next_page': '/login'}),
    url(r'^user/', include('usrprofil.urls')),
    url(r'^reg/', include('usrprofil.urls')),
    url(r'^thanks/$', views.LoginView.as_view(), {'template_name': 'regsuc.html'})]


    #url(r'^/home/regform/$',)
    #url(r'^/home/regform/$', userprofile.views.user_profile, {'template_name': 'userprof.html', 'authentication_form': UserProfileForm}, name='user_profile'),
    #url(r'^profile/(?P<profile_id>[\d]+)/$', views.user_profile, name="user_profile"),