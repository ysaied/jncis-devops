import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2
import routing_interface_service_pb2 as routing__interface__service__pb2


class RoutingInterfaceStub(object):
  """*
  Routing interfaces service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RoutingInterfaceInitialize = channel.unary_unary(
        '/routing.RoutingInterface/RoutingInterfaceInitialize',
        request_serializer=routing__interface__service__pb2.RoutingInterfaceInitializeRequest.SerializeToString,
        response_deserializer=routing__interface__service__pb2.RoutingInterfaceInitializeResponse.FromString,
        )
    self.RoutingInterfaceGet = channel.unary_unary(
        '/routing.RoutingInterface/RoutingInterfaceGet',
        request_serializer=routing__interface__service__pb2.RoutingInterfaceGetRequest.SerializeToString,
        response_deserializer=routing__interface__service__pb2.RoutingInterfaceGetResponse.FromString,
        )
    self.RoutingInterfaceNotificationRegister = channel.unary_stream(
        '/routing.RoutingInterface/RoutingInterfaceNotificationRegister',
        request_serializer=routing__interface__service__pb2.RoutingInterfaceNotificationRegisterRequest.SerializeToString,
        response_deserializer=routing__interface__service__pb2.RoutingInterfaceNotificationResponse.FromString,
        )
    self.RoutingInterfaceNotificationUnregister = channel.unary_unary(
        '/routing.RoutingInterface/RoutingInterfaceNotificationUnregister',
        request_serializer=routing__interface__service__pb2.RoutingInterfaceNotificationUnregisterRequest.SerializeToString,
        response_deserializer=routing__interface__service__pb2.RoutingInterfaceNotificationUnregisterResponse.FromString,
        )
    self.RoutingInterfaceNotificationRefresh = channel.unary_unary(
        '/routing.RoutingInterface/RoutingInterfaceNotificationRefresh',
        request_serializer=routing__interface__service__pb2.RoutingInterfaceNotificationRefreshRequest.SerializeToString,
        response_deserializer=routing__interface__service__pb2.RoutingInterfaceNotificationRefreshResponse.FromString,
        )


class RoutingInterfaceServicer(object):
  """*
  Routing interfaces service
  """

  def RoutingInterfaceInitialize(self, request, context):
    """*
    Service initialize

    A client must first use this RPC to initialize and connect
    to the service, before issuing other RPCs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RoutingInterfaceGet(self, request, context):
    """*
    Get a routing interface by name or index

    A client may use this RPC to query an individual routing interface
    at any time. The client should already know the name or index of
    the interface via notification or any other method.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RoutingInterfaceNotificationRegister(self, request, context):
    """* 
    Notification register

    Request to receive asynchronous notifications of
    of routing interface CHANGED, UP, DOWN and DELETED
    status events.

    After a RoutingInterfaceNotificationRegisterRequest,
    an initial RoutingInterfaceNotificationResponse is sent
    immediately to the client, as a confirmation for the
    request. This response may or may not carry an interface.

    Then, RoutingInterfaceNotificationResponses are
    sent to the client, as a full flash of all the interfaces.

    Subsequently, a RoutingInterfaceNotificationResponse
    will be sent to the client upon a CHANGED, UP, DOWN,
    or DELETED status event of an interface.

    Notification compression:
    When a status event of an interface is pending for a client
    to be notified of, a new status event happens.
    As a net result, a single notification representing the
    latest status and attributes of the interface is sent to
    the client. This should only happen when consecutive events
    happen with extremely small intervals. Examples:

    [1] When a CHANGED event is pending, an UP/DOWN
    event happens. Hence, an UP/DOWN notification
    is sent.
    [2] When a CHANGED/UP/DOWN event is pending, a DELETED
    event happens. Hence, a DELETED notification
    is sent.
    [3] When an UP/DOWN event if pending, a CHANGED
    event happens. Hence, only an UP/DOWN notification
    is sent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RoutingInterfaceNotificationUnregister(self, request, context):
    """* 
    Notification unregister

    Request to stop receiving notifications (i.e. RoutingInterfaceNotificationResponses)
    of routing interface events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RoutingInterfaceNotificationRefresh(self, request, context):
    """* 
    Notification refresh

    Request to receive a refresh of notifications (i.e. RoutingInterfaceNotificationResponses)
    of all routing interfaces, with their current status and attributes.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RoutingInterfaceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RoutingInterfaceInitialize': grpc.unary_unary_rpc_method_handler(
          servicer.RoutingInterfaceInitialize,
          request_deserializer=routing__interface__service__pb2.RoutingInterfaceInitializeRequest.FromString,
          response_serializer=routing__interface__service__pb2.RoutingInterfaceInitializeResponse.SerializeToString,
      ),
      'RoutingInterfaceGet': grpc.unary_unary_rpc_method_handler(
          servicer.RoutingInterfaceGet,
          request_deserializer=routing__interface__service__pb2.RoutingInterfaceGetRequest.FromString,
          response_serializer=routing__interface__service__pb2.RoutingInterfaceGetResponse.SerializeToString,
      ),
      'RoutingInterfaceNotificationRegister': grpc.unary_stream_rpc_method_handler(
          servicer.RoutingInterfaceNotificationRegister,
          request_deserializer=routing__interface__service__pb2.RoutingInterfaceNotificationRegisterRequest.FromString,
          response_serializer=routing__interface__service__pb2.RoutingInterfaceNotificationResponse.SerializeToString,
      ),
      'RoutingInterfaceNotificationUnregister': grpc.unary_unary_rpc_method_handler(
          servicer.RoutingInterfaceNotificationUnregister,
          request_deserializer=routing__interface__service__pb2.RoutingInterfaceNotificationUnregisterRequest.FromString,
          response_serializer=routing__interface__service__pb2.RoutingInterfaceNotificationUnregisterResponse.SerializeToString,
      ),
      'RoutingInterfaceNotificationRefresh': grpc.unary_unary_rpc_method_handler(
          servicer.RoutingInterfaceNotificationRefresh,
          request_deserializer=routing__interface__service__pb2.RoutingInterfaceNotificationRefreshRequest.FromString,
          response_serializer=routing__interface__service__pb2.RoutingInterfaceNotificationRefreshResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routing.RoutingInterface', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
