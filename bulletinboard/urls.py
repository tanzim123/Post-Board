from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.post_view, name='post_view'),

]