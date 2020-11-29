import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2
import management_service_pb2 as management__service__pb2


class ManagementRpcApiStub(object):
  """
  MGD Service Definitions
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExecuteOpCommand = channel.unary_stream(
        '/management.ManagementRpcApi/ExecuteOpCommand',
        request_serializer=management__service__pb2.ExecuteOpCommandRequest.SerializeToString,
        response_deserializer=management__service__pb2.ExecuteOpCommandResponse.FromString,
        )
    self.ExecuteCfgCommand = channel.unary_unary(
        '/management.ManagementRpcApi/ExecuteCfgCommand',
        request_serializer=management__service__pb2.ExecuteCfgCommandRequest.SerializeToString,
        response_deserializer=management__service__pb2.ExecuteCfgCommandResponse.FromString,
        )
    self.GetEphemeralConfig = channel.unary_unary(
        '/management.ManagementRpcApi/GetEphemeralConfig',
        request_serializer=management__service__pb2.GetEphemeralConfigRequest.SerializeToString,
        response_deserializer=management__service__pb2.GetEphemeralConfigResponse.FromString,
        )
    self.EditEphemeralConfig = channel.unary_unary(
        '/management.ManagementRpcApi/EditEphemeralConfig',
        request_serializer=management__service__pb2.EditEphemeralConfigRequest.SerializeToString,
        response_deserializer=management__service__pb2.EditEphemeralConfigResponse.FromString,
        )


class ManagementRpcApiServicer(object):
  """
  MGD Service Definitions
  """

  def ExecuteOpCommand(self, request, context):
    """
    It executes the operational command specified in
    ExecuteOpCommandRequest. This is a streaming api
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteCfgCommand(self, request, context):
    """
    The RPC will enable user to load and commit configuration on a junos
    device
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEphemeralConfig(self, request, context):
    """
    This RPC will return the configuration in the ephemeral database
    for Path specified in the request
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EditEphemeralConfig(self, request, context):
    """
    This RPC will perfom load-configuration and commit in JUNOS in ephemeral
    database
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ManagementRpcApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ExecuteOpCommand': grpc.unary_stream_rpc_method_handler(
          servicer.ExecuteOpCommand,
          request_deserializer=management__service__pb2.ExecuteOpCommandRequest.FromString,
          response_serializer=management__service__pb2.ExecuteOpCommandResponse.SerializeToString,
      ),
      'ExecuteCfgCommand': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteCfgCommand,
          request_deserializer=management__service__pb2.ExecuteCfgCommandRequest.FromString,
          response_serializer=management__service__pb2.ExecuteCfgCommandResponse.SerializeToString,
      ),
      'GetEphemeralConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetEphemeralConfig,
          request_deserializer=management__service__pb2.GetEphemeralConfigRequest.FromString,
          response_serializer=management__service__pb2.GetEphemeralConfigResponse.SerializeToString,
      ),
      'EditEphemeralConfig': grpc.unary_unary_rpc_method_handler(
          servicer.EditEphemeralConfig,
          request_deserializer=management__service__pb2.EditEphemeralConfigRequest.FromString,
          response_serializer=management__service__pb2.EditEphemeralConfigResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'management.ManagementRpcApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
