from django.test import TestCase

class HeartbeatTest(TestCase):
    def test_heartbeat_ok(self):
        response = self.client.get('/heartbeat/')
        self.assertEqual(response.status_code, 200)
