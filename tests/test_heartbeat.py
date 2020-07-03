from django.test import TestCase, override_settings
import django_heartbeat

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

    def test_heartbeat_output(self):
        heartbeat_ok = {'heartbeat': 'ok'}
        heartbeat_output = {'ver': django_heartbeat.__version__}
        heartbeat_ok_and_output = {}
        heartbeat_ok_and_output.update(heartbeat_ok)
        heartbeat_ok_and_output.update(heartbeat_output)
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertDictEqual(response.data, heartbeat_ok_and_output)
