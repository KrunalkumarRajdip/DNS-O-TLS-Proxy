# DNS Proxy with DNS-over-TLS

## Introduction

This project implements a DNS proxy server using Python, which supports DNS-over-TLS (DoT) to encrypt DNS queries. The proxy server listens for DNS queries over TCP port 53 and forwards them to a DNS-over-TLS server.

## Files

- `daemon.py`: Contains the implementation of the DNS proxy server.
- `client.py`: Script to simulate DNS queries and test the DNS proxy server.
- `requirements.txt`: Lists the dependencies required to run the DNS proxy server.
- `Dockerfile`: Dockerfile to build a Docker image for running the DNS proxy server in a container.
- `unittests.py`: Contains unit tests to verify the functionality of the DNS proxy server.
- `README.md`: This file.

## Changes Made

1. Implemented the DNS proxy server in `daemon.py`.
2. Added necessary dependencies to `requirements.txt`.
3. Created a Dockerfile (`Dockerfile`) to containerize the DNS proxy server.
4. Wrote unit tests (`unittests.py`) to validate the functionality of the DNS proxy server.
5. Modified the `client.py` script to simulate DNS queries and test the DNS proxy server.

## Troubleshooting

- **Issue**: Certificate verification failed during DNS-over-TLS connection.
  **Resolution**: Loaded the CA certificates using the `certifi` module in the SSL context.

- **Issue**: DNS queries were timing out.
  **Resolution**: Ensured that the DNS proxy server was correctly forwarding queries to the DNS-over-TLS server.

## Testing the Flow

1. **Testing DNS Proxy Server**:
   - Run `python daemon.py` to start the DNS proxy server.
   - Execute `python client.py` to simulate DNS queries and test the server.

2. **Unit Testing**:
   - Run `python unittests.py` to execute the unit tests.

3. **Docker Container**:
   - Build the Docker image: `docker build -t dns-proxy .`
   - Run the Docker container: `docker run -d -p 8053:8053 dns-proxy`
   - Test using `python client.py` or `dig @localhost -p 8053 example.com +tcp`.

## Setup Instructions

1. Clone the repository: `git clone https://github.com/your_username/dns-proxy.git`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Follow the testing instructions mentioned above to verify the setup.

## Security Concerns

1. **Certificate Management**: Ensure secure storage and rotation of TLS certificates.
2. **Access Control**: Implement proper authentication and authorization mechanisms to control access to the DNS proxy server.
3. **Data Encryption**: Safeguard sensitive information, such as DNS queries and responses, using encryption.
4. **Logging and Monitoring**: Monitor network traffic and logs for any suspicious activities.

## Integration in Microservices Architecture

1. Deploy the DNS proxy server as a microservice within a containerized environment.
2. Implement service discovery mechanisms to route DNS traffic to the proxy server.
3. Utilize container orchestration tools like Kubernetes for deployment and scaling.
4. Integrate with a centralized logging and monitoring system for better visibility and control.

## Further Improvements

1. **Performance Optimization**: Optimize the DNS proxy server for better throughput and response times.
2. **Support for DNSSEC**: Add support for DNS Security Extensions (DNSSEC) to enhance DNS security.
3. **DNS Caching**: Implement DNS caching to reduce latency and improve performance.
4. **Health Checks**: Integrate health checks to ensure the availability and reliability of the DNS proxy server.

---

### Answers to Additional Questions:

1. **Security Concerns**: Security concerns include certificate management, access control, data encryption, and logging/monitoring.
2. **Integration in Microservices Architecture**: Integrate the DNS proxy server as a microservice using containerization and orchestration tools like Kubernetes.
3. **Further Improvements**: Consider optimizations for performance, support for DNSSEC, DNS caching, and implementation of health checks.
