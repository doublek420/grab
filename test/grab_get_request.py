# coding: utf-8
from test.util import build_grab
from test.util import BaseGrabTestCase


class GrabSimpleTestCase(BaseGrabTestCase):
    def setUp(self):
        self.server.reset()

    def test_get(self):
        self.server.response['get.data'] = 'Final Countdown'
        grab = build_grab()
        grab.go(self.server.get_url())
        self.assertTrue(b'Final Countdown' in grab.response.body)

    def test_body_content(self):
        self.server.response['get.data'] = 'Simple String'
        grab = build_grab()
        grab.go(self.server.get_url())
        self.assertEqual(b'Simple String', grab.response.body)
        # self.assertEqual('Simple String' in grab.response.runtime_body)

    def test_status_code(self):
        self.server.response['get.data'] = 'Simple String'
        grab = build_grab()
        grab.go(self.server.get_url())
        self.assertEqual(200, grab.response.code)

    def test_depreated_hammer_mode_options(self):
        self.server.response['get.data'] = 'foo'
        grab = build_grab()
        grab.setup(hammer_mode=True)
        grab.go(self.server.get_url())

        grab.setup(hammer_timeouts=((1, 1), (2, 2)))
        grab.go(self.server.get_url())

    def test_parsing_response_headers(self):
        self.server.response['headers'] = [('Hello', 'Grab')]
        grab = build_grab()
        grab.go(self.server.get_url())
        self.assertTrue(grab.response.headers['Hello'] == 'Grab')
