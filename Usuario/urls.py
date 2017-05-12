from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Usuario import views

urlpatterns = [
    url(r'^usuarios/$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
