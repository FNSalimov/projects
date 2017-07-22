from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'my_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('english.urls', namespace="english")),
    url(r'^admin/', include(admin.site.urls)),
]
