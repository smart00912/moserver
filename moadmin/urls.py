__author__ = 'sean.li'
from django.conf.urls import url


urlpatterns=[
	url(r'^$','index',prefix='moadmin.views'),
	url(r'server_fun_categ/$','server_fun_categ',prefix='moadmin.views'),
    url(r'server_app_categ/$','server_app_categ',prefix='moadmin.views'),
    url(r'server_list/$','server_list',prefix='moadmin.views'),
    url(r'module_list/$','module_list',prefix='moadmin.views'),
    url(r'module_info/$','module_info',prefix='moadmin.views'),
    url(r'module_run/$','module_run',prefix='moadmin.views'),
    url(r'module_add/$','module_add',prefix='moadmin.views'),
    url(r'module_add_post/$','module_add_post',prefix='moadmin.views'),
]
