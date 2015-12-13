from django.conf.urls import url


urlpatterns = [
        url(r'^1/', 'article.views.basic_one'),
        url(r'^2/', 'article.views.template_two'),
        url(r'^3/', 'article.views.template_three_simple'),
        url(r'^articles/all/$', 'article.views.articles'),
        url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
        url(r'^', 'article.views.articles'),
]
