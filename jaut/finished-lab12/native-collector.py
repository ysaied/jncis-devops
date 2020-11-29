import socket
from compiled_jti.telemetry_top_pb2 import TelemetryStream
import compiled_jti.logical_port_pb2

LISTEN_ADDR = "10.2.0.254"
LISTEN_PORT = 30000

if __name__ == "__main__":
    # Create and bind a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((LISTEN_ADDR, LISTEN_PORT))

    # TelemetryStream message object
    telemetry = TelemetryStream()

    # While not interrupted, read from socket, parse and print
    try:
        while True:
            data, addr = s.recvfrom(5000)
            telemetry.ParseFromString(data)
            print telemetry
    except KeyboardInterrupt:
        s.close()
