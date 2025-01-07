# DevOps Engineer Assessment

This repository contains scripts and configurations related to DevOps Engineer assessment. The project includes a script for monitoring CPU usage, steps to troubleshooting a PostgreSQL query, a Dockerfile for containerizing a Laravel application, and a Prometheus exporter for RabbitMQ.

## Overview

This project contains DevOps coding challenges for a technical assessment.

## CPU Monitoring Script

A script to monitor CPU usage of a Laravel backend service that is written with bash scripting language and ansible Playbook. It restarts the service if CPU usage exceeds 80%.

## PostgreSQL Query Troubleshooting

Approach to troubleshoot a slow running PostgreSQL query, including analyzing resource utilization, examining the query complexity and checking locks.

## Dockerfile for Laravel Application

A Dockerfile to containerize the Laravel application using the compatible PHP image with Apache.

## Prometheus RabbitMQ Exporter

A Prometheus exporter that connects to the RabbitMQ HTTP API to gather metrics about queues. It exports `messages`, `messages_ready`, and `messages_unacknowledged` metrics.
