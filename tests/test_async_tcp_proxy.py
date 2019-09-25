from async_tcp_proxy.proxy.async_tcp_proxy import ATcpProxy
from async_tcp_proxy.server.tcp_echo_server import TcpEchoServer

import threading
import time
import unittest

class TestAsyncTcpProxy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._server = TcpEchoServer()
        cls._thread = threading.Thread(target=cls._server.start)
        cls._thread.start()
        time.sleep(0.5) # Allow server to start
        cls._proxy = ATcpProxy()

    @classmethod
    def tearDownClass(cls):
        cls._thread.join()

    def test_proxy_send_one(self):
        payload = 'Hello unittest!'.encode()
        self._proxy.send(payload)
        time.sleep(0.5) # Allow background loop to read message into incoming queue.
        incoming = self._proxy.incoming_q
        self._proxy.stop()
        self.assertTrue(payload in incoming)


    def test_proxy_send_multiple(self):
        pass


if __name__ == "__main__":
    unittest.main()