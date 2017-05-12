from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Classe import views

urlpatterns = [
    url(r'^classes/$', views.ClasseList.as_view()),
    url(r'^classes/(?P<pk>[0-9]+)/$', views.ClasseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
