from django.conf.urls import *
from django_heartbeat.views import HeartBeatView, StaticHeartbeatView

urlpatterns = patterns('',
    url(r'^heartbeat/$', HeartBeatView.as_view(), name='django_heartbeat'),
    url(r'^staticheartbeat/$', StaticHeartbeatView.as_view(), name='django_static_heartbeat'),
)