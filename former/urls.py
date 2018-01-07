from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import getQ,postQ,getAns,individual,login_view,logout_views
from django.conf import settings
from django.contrib.auth import views as auth_views
from former import views as app_views
admin.autodiscover()

urlpatterns =[
<<<<<<< HEAD
=======
	#url(r'^$', app_views.home, name='home'),
>>>>>>> 95ac8cf8c52dc3e7627810cce828ce2763914ca8
	url(r'^newform/$', app_views.getQ),
	url(r'^login/$',app_views.login_view),
	url(r'^logout/$',logout_views),
	url(r'^register/$',app_views.create_user),
	url(r'^$', app_views.all_forms),
	url(r'^(?P<pk>[\w-]+)/$', app_views.getAns, name ='explore_forms'),
    url(r'^post/(?P<pk>[\w-]+)/$',app_views.postQ),
    url(r'^post/(?P<pk>[\w-]+)/(?P<id>[\W-]+)/$',app_views.individual),   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
