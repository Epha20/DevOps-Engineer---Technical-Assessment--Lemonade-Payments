#!/bin/bash

# CPU usage limit
THRESHOLD=80

# Define the service name
SERVICE_NAME="ephrem's laravel backend service"

# To check CPU usage
check_cpu_usage() {
    # Average CPU usage of last one minute
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo "$CPU_USAGE"
}

# restart backend service
restart_service() {
    echo "CPU usage exceeds ${THRESHOLD}%. ${SERVICE_NAME} restarted"
    systemctl restart "$SERVICE_NAME"
}

# main 
CPU_USAGE=$(check_cpu_usage)
echo "Current CPU usage: $CPU_USAGE%"

if (( $(echo "$CPU_USAGE > $THRESHOLD" | bc -l) )); then
    restart_service
else
    echo "CPU usage is within limits."
fi