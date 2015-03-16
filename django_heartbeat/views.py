from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import Permission
from django.core.cache import cache
import logging

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("app.releaser").version
except:
    __version__ = None

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

            request.session['test_value'] = 1
            request.session.save()

            assert request.session["test_value"] == 1
        except Exception:
            logger.exception("Heartbeat Exception")
            output_status = status.HTTP_500_INTERNAL_SERVER_ERROR
            res = 'failed'

        output_data = {}
        output_data['heartbeat'] = res
        output_data['ver'] = __version__

        return Response(output_data, status = output_status)