from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'Printer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url('',include('social.apps.django_app.urls',namespace='social'))
    url(r'^dashboard/$',views.dashboard,name='dashboard'),

    url(r'^Stl_List/$',views.Stl_List,name='Stl_List'),
   # url(r'^Stl_List/Stl_Pr_Select/(?P<pk>\d+)/$',Stl_Pr_Select,name='Stl_Pr_Select'),
    url(r'^Stl_List/Stl_Delete/(?P<pk>\d+)/$',views.Stl_Delete,name='Stl_Delete'),

    url(r'^model_list/$',views.model_list,name='model_list'),
    url(r'^model_list/model_owner/$',views.model_owner,name='model_owner'),
    url(r'^model_list/model_sell/$',views.model_sell,name='model_sell'),



    url(r'^model_list/model_owner/model_modify/(?P<pk>\d+)/$',views.model_modify,name='model_modify'),
]
