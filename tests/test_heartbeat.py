from django.test import TestCase, override_settings
from django_heartbeat.settings import HEARTBEAT_OUTPUT

CACHES_DISABLED = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

HEARTBEAT_OK = {'heartbeat': 'ok'}
HEARTBEAT_OK_AND_OUTPUT = {}
HEARTBEAT_OK_AND_OUTPUT.update(HEARTBEAT_OK)
HEARTBEAT_OK_AND_OUTPUT.update(HEARTBEAT_OUTPUT)

class HeartbeatTest(TestCase):
    def test_heartbeat_ok(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)

    @override_settings(CACHES=CACHES_DISABLED)
    def test_heartbeat_failed(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 500)

    def test_heartbeat_output(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertDictEqual(response.data, HEARTBEAT_OK_AND_OUTPUT)
