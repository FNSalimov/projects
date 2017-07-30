from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^english$', views.english, name='english'),
    url(r'^test$', views.test, name='test'),
    url(r'^fifteen$', views.fifteen, name='fifteen'),
]