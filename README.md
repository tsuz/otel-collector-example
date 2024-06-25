# OpenTelemetry Collector with Prometheus Metrics Collection

This project sets up an OpenTelemetry Collector using Docker to collect Prometheus metrics from a local REST API.

## Prerequisites

- Docker
- Docker Compose
- A local REST API exposing Prometheus metrics

## Setup

1. Clone this repository or create a new directory for this project.

2. Create a `docker-compose.yml` file with the following content:

3. Start the collector

```sh
docker-compose up -d
```

4. Verify the collector is running

```sh
docker-compose ps
```

5. Check the logs to ensure it's collecting metrics

```sh
docker-compose logs otel-collector
````

