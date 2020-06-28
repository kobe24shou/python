"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import  views  # 引入对应的包

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cur_time',views.cur_time), # 添加路径和对应的函数 (对应的函数写到views里面),尖括号，表示必须以cur_time开头
    
    url(r"^userInfo",views.userInfo),


    url(r'^articles/2003/$', views.special_case_2003),
    # ^以开头 $以结尾  --》以a 开头，以/ 结尾  views.special_case_2003 表示视图函数
    url(r'^articles/[0-9]{4}/$', views.year_archive),
    # 后面4个0到9的数字
    # 从上到下一次匹配，2003 符合第一种情况，第2个就不会匹配

    url(r'^articles1/([0-9]{4})/$', views.year_archive1),  # no_named group
    # 给视图函数 传参数

    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # {4} 重复4次 {2} 重复2次  2个括号就有要传2个参数

    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
    # #  year month day 名字和views 里面对应接受的参数需要一样

    url(r'^index1',views.index1,{"name":'ls'}),
    # 传默认参数，这个name和 urls 里面的name 对应


    url(r'^index', views.index, name='bieming'),
    # 前端请求和后端处理 使用别名
    # 模板语言  {% url 'bieming' %}


]