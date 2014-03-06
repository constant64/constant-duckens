#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('esihapp.views',
    # Examples:
    # url(r'^$', 'esih.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','home'),#url page d'acceuil
    url(r'^codage/$','Code_cour'),#url pour code cours
    url(r'^programme/$','Prog'),#url pour code programme
    url(r'^prof/$','prof'),#url pour professeur
    url(r'^list/$','listerc'),#url pour lister cours
    url(r'^modc/(\d+)/$','CourM'),#url pour modifier cours
    url(r'^listp/$','listerp'),#url pour lister programme
    url(r'^modp/(\d+)/$','ProgM'),#url pour modifier programme
    url(r'^admin/', include(admin.site.urls)),
    url(r'^supp/(\d+)/$','ProgS'),
    url(r'^supc/(\d+)/$','CoursS'),
    url(r'^supprof/(\d+)/$','ProfS'),
    url(r'^desc/$','Desc'),
    url(r'^nouvi/$','nouvi'),
    url(r'^nouvc/$','nouvc'),
    url(r'^nouvg/$','nouvg'),
    url(r'^cv/(\d+)/$','CVP'),
    url(r'^listprof/$','listerprof'),
    url(r'^modprof/(\d+)/$','ProfM'),
    url(r'^login/$','login'),
    url(r'^logout/$','logout'),
    url(r'^listerdesc/$','listerdesc'),



)
