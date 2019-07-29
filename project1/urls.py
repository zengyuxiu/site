from django.conf.urls import url
from django.urls import include, path

import project1.views
import Index.views
import project0.views

urlpatterns = [

    url(r'^$', project1.views.index, name='p1_index'),
    url(r'index/', Index.views.index, name='main_index'),
    #url(r'p0_index/', project0.views.index, name='p0_index'),
    url(r'^project1-name1/$', project1.views.name_1, name='p1n1'),
    url(r'^project1-name2/$', project1.views.name_2, name='p1n2'),
    url(r'^project1-name3/$', project1.views.name_3, name='p1n3'),
    url(r'^project1-name4/$', project1.views.name_4, name='p1n4'),
    url(r'^project1-name5/$', project1.views.name_5, name='p1n5'),
]
