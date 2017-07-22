from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^english$', views.english, name='english'),
    url(r'^test$', views.test, name='test'),
    url(r'^fifteen$', views.fifteen, name='fifteen'),
    url(r'^news$', views.news, name='news'),
    url(r'^news/profile$', views.profile, name='profile'),
    url(r'^news/add/([0-9]+)$', views.add, name='add'),
]