# DNS Proxy with DNS-over-TLS

## Introduction

This project implements a DNS proxy server using Python, which supports DNS-over-TLS (DoT) to encrypt DNS queries. The proxy server listens for DNS queries over TCP port 53 and forwards them to a DNS-over-TLS server.

## Files

- `dns-proxy.py`: Contains the implementation of the DNS proxy server.
- `client.py`: Script to simulate DNS queries and test the DNS proxy server(Not the Perfect one, Did not spend enough time on it).
- `requirements.txt`: Lists the dependencies required to run the DNS proxy server(Not much as of now).
- `Dockerfile`: Dockerfile to build a Docker image for running the DNS proxy server in a container.
- `testDNSOTLSs.py`: Contains unit tests to verify the functionality of the DNS proxy server.

## Approach

1. Implemented the DNS proxy server in `dns-proxy.py`.
   - Used SSL, Socket, Threading, Logging, OS and Certifi Modules
   - Cloudflare DNS-TLS server
   - Handle and Listener functions
   - Certifi certs to add in SSL Context
   - Binded Daemon to be used from 0.0.0.0 and 8053 port since docker loop backing the daemon and outside of accesibilty was not possible.(A debatable move but for a challange I was minimal as of now)
1. Added necessary dependencies to `requirements.txt`.
2. Created a Dockerfile (`Dockerfile`) to containerize the DNS proxy server.
3. Wrote unit tests (`testDNSOTLSs.py`) to validate the functionality of the DNS proxy server.
   - Unit testing with help of importing DNS-TLS daemon we created.
   - Used threading to run main function of daemon and use the behaviour of the script and test the connections in local.
   - Only to be used in local not anywhere else.
4. Modified the `client.py` script to simulate DNS queries and test the DNS proxy server.
   - Tried creating a client script but was able to validate workflow using DIG command.

## Testing the Flow

1. **Testing DNS Proxy Server**:
   - Run `python dns-proxy.py` to start the DNS proxy server.
 
#### Using `dig` Command for DNS Queries in DNS-over-TLS (DoT) Setup

In the context of our DNS-over-TLS (DoT) setup, the `dig` command can be used to perform DNS queries and ensure that the entries are coming from a TLS server and encrypted. Here's how we can use `dig` in our specific scenario:

### Usage of `dig` Command with DoT

#### Basic Syntax:
```bash
dig @server -p port +tcp [hostname] [query_type]
```

### Verifying Encrypted DNS Queries
To ensure that DNS queries are encrypted and sent over TLS, follow these steps:
1. Specify TCP Protocol: Use the +tcp option to specify the TCP protocol, which is required for DNS-over-TLS (DoT).
```bash
dig @localhost -p 8053 +tcp example.com A
```
2. Check for DNSSEC Flag:
Include the +dnssec option to check for the DO (DNSSEC OK) flag in the response header, indicating DNSSEC is enabled, which often accompanies encrypted DNS queries.
```bash
dig @localhost -p 8053 +dnssec example.com A
```
3. Verify Certificate:
Inspect the certificate details received in the response to ensure it matches the expected certificate from the TLS server.
```bash
dig @localhost -p 8053 +short +tcp example.com A
```
By using these options with the dig command, we can verify that DNS queries are encrypted and securely transmitted over TLS in our DoT setup.

2. **Unit Testing**:
   - Run `python testDNSOTLSs.py` to execute the unit tests.

3. **Docker Container**:
   - Build the Docker image:
    ```bash
   docker build -t dns-proxy .
    ```
   - Run the Docker container:
     ```bash
      docker run -d -p 8053:8053 --name my-dns-proxy-container -v ./logs:/app/log my-dns-proxy
     ```
   - Test using 
     ```bash
     dig @localhost -p 8053 example.com +tcp
     ```

## Setup Instructions

1. Unzip the folder or added in a Git repo then clone the repository. 
2. Install dependencies: `pip install -r requirements.txt`.
3. Run `python dns-proxy.py` to start the DNS proxy server in Local
4. If Having issues testing it or want to run this inside a container then build the image from dockerfile and run as per the instructions given above.

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

1. **Performance Optimization**: Optimize the DNS proxy server for better throughput and response times, Might reengineer in Go. 
2. **Support for DNSSEC**: Add support for DNS Security Extensions (DNSSEC) to enhance DNS security.
3. **DNS Caching**: Implement DNS caching to reduce latency and improve performance.
4. **Health Checks**: Integrate health checks to ensure the availability and reliability of the DNS proxy server, Readiness and liveness probes.

---
