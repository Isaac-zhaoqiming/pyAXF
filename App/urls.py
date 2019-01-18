from django.conf.urls import url, include

from App import views

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^market/$',views.market,name='market'),
    url(r'^queryfood/(\d+)/(\d+)/(\d+)/$',views.queryfood,name='queryfood'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^subcart/$',views.subcart,name='subcart'),
    url(r'^changestate/$',views.changestate,name='changestate'),
    url(r'^allselect/$',views.allselect,name='allselect'),
]