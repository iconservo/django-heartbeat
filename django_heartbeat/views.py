from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import Permission
from django.core.cache import cache
import logging

logger = logging.getLogger("django.heartbeat")

class HeartBeatView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        output_status = status.HTTP_200_OK
        res = 'ok'
        try:
            Permission.objects.get(id = 1) #django permission. Should be always available
            cache.set('test', 1)
            cache_get = cache.get('test')
            if cache_get != 1:
                raise ValueError
        except Exception:
            logger.exception("Heartbeat Exception")
            output_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            res = 'failed'

        return Response({'heartbeat': res }, status = output_status)