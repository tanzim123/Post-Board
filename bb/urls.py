from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'login/', views.user_login, name='login'),
    url(r'create/', views.post, name='createpost'),
    url(r'^$', views.register, name='register'),

]