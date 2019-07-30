from django.conf.urls import url
from django.urls import include, path

import project0.views
import Index.views
import project1.views
import project2.views

urlpatterns = [
    url(r'^$', project2.views.index, name='p2_index'),
    url(r'p1_index/', project1.views.index, name='p1_index'),
    url(r'p0_index/', project0.views.index, name='p0_index'),
    url(r'index/', Index.views.index, name='main_index'),
    url(r'^project2-name1/$', project2.views.name_1, name='p2n1'),
    url(r'^project2-name2/$', project2.views.name_2, name='p2n2'),
]