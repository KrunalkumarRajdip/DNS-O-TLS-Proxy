# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the daemon script and requirements file into the container
COPY dns-proxy.py requirements.txt /app/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8053

# Create a directory to store log files
RUN mkdir /app/logs

# Set up a volume for log file storage
VOLUME /app/logs

# Command to run the daemon script
CMD ["python", "dns-proxy.py"]