from compiled_jti.agent_pb2 import *
import grpc

if __name__ == "__main__":
    channel = grpc.insecure_channel("172.25.11.2:32767")

    path = Path(path="/components", sample_frequency=5000)
    request = SubscriptionRequest(path_list=[path])

    oc_telemetry_stub = OpenConfigTelemetryStub(channel)

    for data in oc_telemetry_stub.telemetrySubscribe(request, 3600):
        print data
