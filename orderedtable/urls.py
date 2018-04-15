from django.conf.urls import include, url
from django.contrib import admin

import orderedtable
from orderedtable import views

app_name="orderedtable"

urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'^import-json/$', views.import_json,name="import_json"),
    url(r'^project-list/$', views.project_list,name="project_list"),
    url(r'^empty-list/$', views.delete_table,name="delete_table"),
    url(r'^multiple-sorting/$', views.multiple_sorting,name="multiple_sorting"),
    url(r'^sort-by = (?P<pk>[\w-]+)/$', views.sorted,name="sorted"),
]
