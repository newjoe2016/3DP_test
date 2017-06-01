from django.conf.urls import include, url
from django.contrib import admin
from Printapp import views
from Printer import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'Printer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url('',include('social.apps.django_app.urls',namespace='social'))
    url(r'^printer/',include('Printapp.urls'),name='printer'),
    url(r'^index/$',views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',views.login),
    url(r'^accounts/logout/$',views.logout),
    url(r'^accounts/register/$', views.register),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
