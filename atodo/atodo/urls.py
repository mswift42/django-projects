from django.conf.urls import patterns, include, url
from todolist import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^report/', views.status_report, name='report'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('todolist.urls')),
    url(r'^report/', include('todolist.urls')),
)
