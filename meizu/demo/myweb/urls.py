from django.conf.urls import url
from . import views

urlpatterns = [

    #商城模板套用
    url(r'^$', views.index,name='index'), #  商城首页
    url(r'^list$', views.list,name='list'), #  商城列表页
    url(r'^detail(?P<gid>[0-9]+)$', views.detail,name='detail'), #  商城详情页

    # 商城购物车
    url(r'^cartadd$', views.cartadd,name='cartadd'),
    url(r'^cartshow$', views.cartshow,name='cartshow'), 
    url(r'^cartchange$', views.cartchange,name='cartchange'),
    url(r'^cartdel(?P<gid>[0-9]+)$', views.cartdel,name='cartdel'),
    url(r'^cartclear$', views.cartclear,name='cartclear'),


    # 订单页
    url(r'^ordera$', views.ordera,name='ordera'),
    url(r'^orderb$', views.orderb,name='orderb'),
    url(r'^orderadd$', views.orderadd,name='orderadd'),
    url(r'^ordershow$', views.ordershow,name='ordershow'),


    








    # 商城登录页
    url(r'^login$', views.login,name='login'), 
    url(r'^dologin$', views.dologin,name='dologin'),
    url(r'^logout$', views.logout,name='logout'), 




 


]