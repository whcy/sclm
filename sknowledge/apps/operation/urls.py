from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^(?P<folder_id>\d+)/$',views.directory_listing,name='directory_listing'),
    # url(r'^(?P<folder_name>[\w\-]+)/$',views.directory_listing,name='directory_listing'),
    url(r'^index/$', views.index, name='index'),
    url(r'^phone_bind/$', views.phone_bind, name='phone_bind'),
    url(r'^send_msg/$', views.send_msg, name='send_msg')

]
