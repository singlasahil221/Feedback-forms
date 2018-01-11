from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import getAns,individual,logout_views
from django.conf import settings
from django.contrib.auth import views as auth_views
from former import views as app_views
admin.autodiscover()

urlpatterns =[
	#url(r'^$', app_views.home, name='home'),
	url(r'^$', app_views.getQ),
	url(r'^login/$',auth_views.login,kwargs={'redirect_authenticated_user':True,'template_name':'log.html'}),
	url(r'^logout/$',logout_views),
	url(r'^register/$',app_views.create_user),
	#url(r'^all/$', app_views.index.as_view()),
	url(r'^(?P<pk>[\w-]+)/$', app_views.getAns, name ='explore_forms'),
    url(r'^post/(?P<pk>[\w-]+)/$',app_views.postQ),
    url(r'^post/(?P<pk>[\w-]+)/(?P<id>[\W-]+)/$',app_views.individual),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
