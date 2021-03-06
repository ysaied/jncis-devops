import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2
import agent_pb2 as agent__pb2


class OpenConfigTelemetryStub(object):
  """Interface exported by Agent
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.telemetrySubscribe = channel.unary_stream(
        '/telemetry.OpenConfigTelemetry/telemetrySubscribe',
        request_serializer=agent__pb2.SubscriptionRequest.SerializeToString,
        response_deserializer=agent__pb2.OpenConfigData.FromString,
        )
    self.cancelTelemetrySubscription = channel.unary_unary(
        '/telemetry.OpenConfigTelemetry/cancelTelemetrySubscription',
        request_serializer=agent__pb2.CancelSubscriptionRequest.SerializeToString,
        response_deserializer=agent__pb2.CancelSubscriptionReply.FromString,
        )
    self.getTelemetrySubscriptions = channel.unary_unary(
        '/telemetry.OpenConfigTelemetry/getTelemetrySubscriptions',
        request_serializer=agent__pb2.GetSubscriptionsRequest.SerializeToString,
        response_deserializer=agent__pb2.GetSubscriptionsReply.FromString,
        )
    self.getTelemetryOperationalState = channel.unary_unary(
        '/telemetry.OpenConfigTelemetry/getTelemetryOperationalState',
        request_serializer=agent__pb2.GetOperationalStateRequest.SerializeToString,
        response_deserializer=agent__pb2.GetOperationalStateReply.FromString,
        )
    self.getDataEncodings = channel.unary_unary(
        '/telemetry.OpenConfigTelemetry/getDataEncodings',
        request_serializer=agent__pb2.DataEncodingRequest.SerializeToString,
        response_deserializer=agent__pb2.DataEncodingReply.FromString,
        )


class OpenConfigTelemetryServicer(object):
  """Interface exported by Agent
  """

  def telemetrySubscribe(self, request, context):
    """Request an inline subscription for data at the specified path.
    The device should send telemetry data back on the same
    connection as the subscription request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def cancelTelemetrySubscription(self, request, context):
    """Terminates and removes an exisiting telemetry subscription
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTelemetrySubscriptions(self, request, context):
    """Get the list of current telemetry subscriptions from the
    target. This command returns a list of existing subscriptions
    not including those that are established via configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTelemetryOperationalState(self, request, context):
    """Get Telemetry Agent Operational States
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDataEncodings(self, request, context):
    """Return the set of data encodings supported by the device for
    telemetry data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OpenConfigTelemetryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'telemetrySubscribe': grpc.unary_stream_rpc_method_handler(
          servicer.telemetrySubscribe,
          request_deserializer=agent__pb2.SubscriptionRequest.FromString,
          response_serializer=agent__pb2.OpenConfigData.SerializeToString,
      ),
      'cancelTelemetrySubscription': grpc.unary_unary_rpc_method_handler(
          servicer.cancelTelemetrySubscription,
          request_deserializer=agent__pb2.CancelSubscriptionRequest.FromString,
          response_serializer=agent__pb2.CancelSubscriptionReply.SerializeToString,
      ),
      'getTelemetrySubscriptions': grpc.unary_unary_rpc_method_handler(
          servicer.getTelemetrySubscriptions,
          request_deserializer=agent__pb2.GetSubscriptionsRequest.FromString,
          response_serializer=agent__pb2.GetSubscriptionsReply.SerializeToString,
      ),
      'getTelemetryOperationalState': grpc.unary_unary_rpc_method_handler(
          servicer.getTelemetryOperationalState,
          request_deserializer=agent__pb2.GetOperationalStateRequest.FromString,
          response_serializer=agent__pb2.GetOperationalStateReply.SerializeToString,
      ),
      'getDataEncodings': grpc.unary_unary_rpc_method_handler(
          servicer.getDataEncodings,
          request_deserializer=agent__pb2.DataEncodingRequest.FromString,
          response_serializer=agent__pb2.DataEncodingReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'telemetry.OpenConfigTelemetry', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
