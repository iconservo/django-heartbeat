from django.test import TestCase, override_settings

CACHES_DISABLED = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

HEARTBEAT_OUTPUT_SAMPLE = {'foo': 'bar'}

class HeartbeatTest(TestCase):
    def test_heartbeat_ok(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)

    @override_settings(CACHES=CACHES_DISABLED)
    def test_heartbeat_failed(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 500)

    @override_settings(HEARTBEAT_OUTPUT=HEARTBEAT_OUTPUT_SAMPLE)
    def test_heartbeat_output(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
