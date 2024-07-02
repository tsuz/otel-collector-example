from http.server import HTTPServer, BaseHTTPRequestHandler
import gzip
import io
from opentelemetry.proto.collector.metrics.v1.metrics_service_pb2 import ExportMetricsServiceRequest
from google.protobuf.json_format import MessageToJson
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            # Decompress the data
            with gzip.GzipFile(fileobj=io.BytesIO(post_data), mode='rb') as f:
                decompressed_data = f.read()
            
            # Parse the protobuf message
            metrics_request = ExportMetricsServiceRequest()
            metrics_request.ParseFromString(decompressed_data)
            
            # Convert to JSON for easier reading
            json_output = MessageToJson(metrics_request)
            parsed_json = json.loads(json_output)
            
            # Extract and print metric values
            for resource_metrics in parsed_json.get('resourceMetrics', []):
                resource = resource_metrics.get('resource', {})
                print(f"Resource: {resource}")
                
                for scope_metrics in resource_metrics.get('scopeMetrics', []):
                    scope = scope_metrics.get('scope', {})
                    print(f"Scope: {scope}")
                    
                    for metric in scope_metrics.get('metrics', []):
                        name = metric.get('name')
                        description = metric.get('description')
                        unit = metric.get('unit')
                        
                        print(f"\nMetric: {name}")
                        print(f"Description: {description}")
                        print(f"Unit: {unit}")
                        
                        data_points = metric.get('gauge', {}).get('dataPoints', []) or \
                                      metric.get('sum', {}).get('dataPoints', []) or \
                                      metric.get('histogram', {}).get('dataPoints', [])
                        
                        for point in data_points:
                            timestamp = point.get('timeUnixNano')
                            value = point.get('asDouble') or point.get('asInt') or "N/A"
                            print(f"Timestamp: {timestamp}, Value: {value}")
                        
                        print()  # Extra line for readability

        except Exception as e:
            print(f"Error processing data: {e}")

        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(('127.0.0.1', 8080), SimpleHTTPRequestHandler)
print("Server running on port 8080")
httpd.serve_forever()
