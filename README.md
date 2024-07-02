# OpenTelemetry Collector with Prometheus Metrics Collection

This project sets up an OpenTelemetry Collector using Docker to collect Prometheus metrics from a local REST API.

## Prerequisites

- Docker
- Docker Compose
- A local REST API exposing Prometheus metrics

## Setup OTEL

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

## Setup HTTP Receiver

OTEL receives the messages and sends to HTTP endpoint at localhost:8080.

### Pre-requisites

- venv
- Python 3

### Run 

```python
python env
python3 -m venv myenv
source myenv/bin/activate
pip install protobuf opentelemetry-proto
python3 metric_receiver.py
```

If run successfully, one should see the logs below.

<summary>
<details>

```

Metric: kafka_producer_failed_authentication_total
Description: The total number of connections with failed authentication
Unit: None
Timestamp: 1719897207780000000, Value: N/A


Metric: executor_pool_max_threads
Description: The maximum allowed number of threads in the pool
Unit: None
Timestamp: 1719897207780000000, Value: 2147483647.0
Timestamp: 1719897207780000000, Value: 2147483647.0


Metric: kafka_consumer_coordinator_sync_time_avg
Description: The average time taken for a group sync
Unit: None
Timestamp: 1719897207780000000, Value: 15.0


Metric: kafka_producer_records_per_request_avg
Description: The average number of records per request.
Unit: None
Timestamp: 1719897207780000000, Value: 1.0


Metric: kafka_producer_request_total
Description: The total number of requests sent
Unit: None
Timestamp: 1719897207780000000, Value: 6.0


```

</details>
</summary>