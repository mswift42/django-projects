from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
                       url(r'^report', views.status_report, name='report')
)
