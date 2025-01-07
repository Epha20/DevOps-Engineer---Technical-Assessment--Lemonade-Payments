# Ephrem Sisay- DevOps engineer candidate
# Coding Challenge

import os
import time
import requests
import logging
from prometheus_client import start_http_server, Gauge
# A library that collects and exposes metrics to Prometheus
# start_http_server function initializes an HTTP server that listens on a specified port in this case 8000
# Gauge represent value that can increase or decrease over time.


# Configure logging for extra layer of visibility
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# metrics definition to read information about all queues in all vhosts:
RABBITMQ_MESSAGES = Gauge(
    'rabbitmq_individual_queue_messages',
    'Total count of messages in queue',
    ['host', 'vhost', 'name']  
)

RABBITMQ_MESSAGES_READY = Gauge(
    'rabbitmq_individual_queue_messages_ready',
    'Count of ready messages in queue',
    ['host', 'vhost', 'name'] 
)

RABBITMQ_MESSAGES_UNACKNOWLEDGED = Gauge(
    'rabbitmq_individual_queue_messages_unacknowledged',
    'Count of unacknowledged messages in queue',
    ['host', 'vhost', 'name']  
)

# API variables
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')  # Hostname
RABBITMQ_USER = os.getenv('RABBITMQ_USER')  # Username
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')  # Password

# Used to adjust the frequency of metric collection here it is set 30 seconds
SCRAPE_INTERVAL = int(os.getenv('SCRAPE_INTERVAL', 30)) 

def fetch_rabbitmq_metrics():
    """
    updates Prometheus 
    metrics based on the response.
    """
    
    # RabbitMQ management API URL
    url = f'http://{RABBITMQ_HOST}:15672/api/queues'
    
    try:
        # Send a GET request to the API with basic authentication
        response = requests.get(url, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
        response.raise_for_status()  
        
        queues = response.json()  # Parse the JSON response
        
        # check every queue
        for queue in queues:

            name = queue['name']  
            vhost = queue['vhost']  
            messages = queue['messages']  
            messages_ready = queue['messages_ready']  
            messages_unacknowledged = queue['messages_unacknowledged'] 

            # Update Prometheus metrics with extracted data to be set as a target data
            RABBITMQ_MESSAGES.labels(RABBITMQ_HOST, vhost, name).set(messages)
            RABBITMQ_MESSAGES_READY.labels(RABBITMQ_HOST, vhost, name).set(messages_ready)
            RABBITMQ_MESSAGES_UNACKNOWLEDGED.labels(RABBITMQ_HOST, vhost, name).set(messages_unacknowledged)
    
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching metrics: {e}")  # Log error to check if requests fail

if __name__ == '__main__':

    start_http_server(8000)  

    while True:
        fetch_rabbitmq_metrics()  # Fetch and update metrics from RabbitMQ
        time.sleep(SCRAPE_INTERVAL)  # Wait for SCRAPE_INTERVAL sec
