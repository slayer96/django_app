__author__ = 'ghost'
from django.conf.urls import url, patterns
from loginsys import views
urlpatterns = [
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register')
]
