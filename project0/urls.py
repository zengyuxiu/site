from django.conf.urls import url
from django.urls import include, path

import project0.views
import Index.views
import project1.views

urlpatterns = [
    url(r'^$', project0.views.index, name='p0_index'),
    url(r'p1_index/', project1.views.index, name='p1_index'),
    url(r'index/', Index.views.index, name='main_index'),
    url(r'^project0-name1/$', project0.views.name_1, name='p0n1'),
    url(r'^project0-name2/$', project0.views.name_2, name='p0n2'),
    url(r'^project0-name3/$', project0.views.name_3, name='p0n3'),
    url(r'^project0-name4/$', project0.views.name_4, name='p0n4'),
]