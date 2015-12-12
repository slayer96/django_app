from django.conf.urls import url,include
import article

urlpatterns = [
        url(r'^1/', 'article.views.basic_one'),
        url(r'^2/', 'article.views.template_two'),
        url(r'^3/', 'article.views.template_three_simple')
]
