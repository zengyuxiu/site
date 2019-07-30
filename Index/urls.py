from django.conf.urls import url
from django.urls import include, path
import Index.views

import project1.views
import project0.views
urlpatterns = [
    path('p0_index/', project0.views.index, name='p0_index'),
    path('p1_index/', project1.views.index, name='p1_index'),
    path('p2_index/', project1.views.index, name='p2_index'),
    url(r'^$', Index.views.index, name='Index'),
    url(r'^charts/$', Index.views.charts, name='Charts'),
    url(r'^tables/$', Index.views.tables, name='Tables'),
    url(r'^indexData/$', Index.views.DataIndex, name='IndexData'),
]
