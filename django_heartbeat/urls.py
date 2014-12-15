from django.conf.urls import *
from django_heartbeat.views import HeartBeatView

urlpatterns = patterns('',
    url(r'^api/heartbeat/$', HeartBeatView.as_view(), name='django_heartbeat'),
)