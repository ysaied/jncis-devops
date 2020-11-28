#! /usr/bin/python

from jnx_authentication_service_pb2_grpc import Authentication
from jnx_authentication_service_pb2 import LoginRequest
from agent_pb2_grpc import OpenConfigTelemetryStub
from agent_pb2 import Path, SubscriptionRequest
import grpc
import sys

app_device = "192.0.0.45"
app_port = "32767"
app_username = "ysaied"
app_password = "yasser123"
app_client = "SampleApp"
app_timeout = 10
app_freq = 5000
app_sensor = "/interface/interface[name='ge-0/0/0']/subinterfaces/subinterface[index='0']/state/counters"


if __name__ == "__main__":
    channel = grpc.insecure_channel(app_device+":"+app_port)
    auth_stub = Authentication(channel)
    login_request = LoginRequest(username=app_username, password=app_password, client_id=app_client)
    login_responce = auth_stub.Login(login_request, app_timeout)
    if login_responce is not True:
        print ("Error; gRPC server connection failed!!!", login_responce.result)
        sys.exit(1)
    telemetry_stub = OpenConfigTelemetryStub(channel)
    path1 = Path(path=app_sensor, sample_frequency=app_freq)
    request = SubscriptionRequest(path_list=[path1])
    print ("Telemetry sensor data:")
    for data in telemetry_stub.telemetrySubscribe(request, app_time):
        print data



