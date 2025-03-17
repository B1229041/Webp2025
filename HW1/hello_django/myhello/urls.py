from django.urls import path
from . import views


urlpatterns = [
#    path('', views.HelloAPIView.as_view(), name='index'),
    path('add', views.add_post, name='add_post'),
    path('list', views.list_post, name='list_post'),
    path('addcourse', views.addcourse_course, name='addcourse_course'),
    path('courselist', views.courselist_course, name='courselist_course'),
]