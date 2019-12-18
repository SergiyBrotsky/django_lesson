from django.conf.urls import url, include
from blog import views 


urlpatterns = [
    url(r'^$', views.PostlistView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'post/(?P<pk>\d+)/edit/$', views.UpdateView.as_view(), name='post_edit'),


]