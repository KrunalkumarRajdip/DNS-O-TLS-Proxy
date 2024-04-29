import socket
import ssl
import threading
import logging
import os
import certifi

# DNS-over-TLS server to connect
DNS_TLS_SERVER = '1.1.1.1'
DNS_TLS_PORT = 853


# Create a log directory if it doesn't exist
LOG_DIR = 'log'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging
logging.basicConfig(filename=os.path.join(LOG_DIR, 'daemon.log'), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(client_socket):
    # Receive DNS query from client
    data = client_socket.recv(1024)
    
    if data:
        # Create an SSL context
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(certifi.where())
        # context.load_cert_chain(SSL_CERT_FILE, SSL_KEY_FILE)
        
        # Create a TCP socket to connect to DNS-over-TLS server
        with socket.create_connection((DNS_TLS_SERVER, DNS_TLS_PORT)) as tcp_socket:
            with context.wrap_socket(tcp_socket, server_hostname=DNS_TLS_SERVER) as tls_socket:

                # Send DNS query to DNS-over-TLS server
                tls_socket.sendall(data)
                
                # Receive response from DNS-over-TLS server
                response = tls_socket.recv(4096)
                
                # Send response back to client
                client_socket.sendall(response)

                # Log the request and response
                logging.info(f"Received request from {client_socket.getpeername()}: {data}")
                logging.info(f"Sent response to {client_socket.getpeername()}: {response}")

def dns_listener():
    # Create a TCP socket to listen for DNS queries
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        # Allow reusing the address
        tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind to port 53
        # container_ip = socket.gethostbyname(socket.gethostname())
        tcp_socket.bind(('0.0.0.0', 8053))
        tcp_socket.listen(5)
        logging.info("DNS over TCP daemon is listening on port 53...")
        
        while True:
            # Accept incoming connections
            client_socket, _ = tcp_socket.accept()
            logging.info(f"Incoming connection from {client_socket.getpeername()}...")
            
            # Handle client in a new thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

def main():
    # Start DNS listener daemon
    dns_listener()

if __name__ == "__main__":
    main()
