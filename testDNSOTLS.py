import unittest
import socket
import threading
import time

# Import the daemon script for testing
import daemon

class TestDNSProxy(unittest.TestCase):
    def setUp(self):
        # Start the DNS proxy daemon in a separate thread
        self.daemon_thread = threading.Thread(target=daemon.main)
        self.daemon_thread.start()
        # Allow some time for the daemon to start
        time.sleep(1)

    def tearDown(self):
        # Stop the DNS proxy daemon
        self.daemon_thread.join()

    def test_dns_query(self):
        # Simulate a client connecting to the DNS proxy
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('127.0.0.1', 8053))
            # Send a DNS query
            client_socket.sendall(b'\xAA\xAA\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x02\x65\x78\x03\x63\x6F\x6D\x00\x00\x01\x00\x01')
            # Receive response from the daemon
            response = client_socket.recv(1024)
            # Assert that the response is not empty
            self.assertTrue(response)

    # Add more test cases for different scenarios if needed

if __name__ == '__main__':
    unittest.main()