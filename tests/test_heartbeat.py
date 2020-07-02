from django.test import TestCase, override_settings

CACHES_DISABLED = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

class HeartbeatTest(TestCase):
    def test_heartbeat_ok(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)

    @override_settings(CACHES=CACHES_DISABLED)
    def test_heartbeat_failed(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 500)
