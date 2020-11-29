import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import mpls_api_service_pb2 as mpls__api__service__pb2
import mpls_api_service_pb2 as mpls__api__service__pb2
import mpls_api_service_pb2 as mpls__api__service__pb2
import mpls_api_service_pb2 as mpls__api__service__pb2
import mpls_api_service_pb2 as mpls__api__service__pb2
import mpls_api_service_pb2 as mpls__api__service__pb2


class MplsApiStub(object):
  """*
  Following are services to get the appropriate information required to do
  a ping to the LSP.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.LspPingGetRsvpInfo = channel.unary_unary(
        '/routing.MplsApi/LspPingGetRsvpInfo',
        request_serializer=mpls__api__service__pb2.RsvpLspPingInfoRequest.SerializeToString,
        response_deserializer=mpls__api__service__pb2.RsvpLspPingInfoReply.FromString,
        )
    self.LspPingGetLdpInfo = channel.unary_unary(
        '/routing.MplsApi/LspPingGetLdpInfo',
        request_serializer=mpls__api__service__pb2.LdpLspPingInfoRequest.SerializeToString,
        response_deserializer=mpls__api__service__pb2.LdpLspPingInfoReply.FromString,
        )
    self.LspPingGetVpnInfo = channel.unary_unary(
        '/routing.MplsApi/LspPingGetVpnInfo',
        request_serializer=mpls__api__service__pb2.VpnLspPingInfoRequest.SerializeToString,
        response_deserializer=mpls__api__service__pb2.VpnLspPingInfoReply.FromString,
        )


class MplsApiServicer(object):
  """*
  Following are services to get the appropriate information required to do
  a ping to the LSP.
  """

  def LspPingGetRsvpInfo(self, request, context):
    """* Service to get the RSVP LSP information 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LspPingGetLdpInfo(self, request, context):
    """* Service to get the LDP LSP information 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LspPingGetVpnInfo(self, request, context):
    """* Service to get the VPN LSP information 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MplsApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'LspPingGetRsvpInfo': grpc.unary_unary_rpc_method_handler(
          servicer.LspPingGetRsvpInfo,
          request_deserializer=mpls__api__service__pb2.RsvpLspPingInfoRequest.FromString,
          response_serializer=mpls__api__service__pb2.RsvpLspPingInfoReply.SerializeToString,
      ),
      'LspPingGetLdpInfo': grpc.unary_unary_rpc_method_handler(
          servicer.LspPingGetLdpInfo,
          request_deserializer=mpls__api__service__pb2.LdpLspPingInfoRequest.FromString,
          response_serializer=mpls__api__service__pb2.LdpLspPingInfoReply.SerializeToString,
      ),
      'LspPingGetVpnInfo': grpc.unary_unary_rpc_method_handler(
          servicer.LspPingGetVpnInfo,
          request_deserializer=mpls__api__service__pb2.VpnLspPingInfoRequest.FromString,
          response_serializer=mpls__api__service__pb2.VpnLspPingInfoReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routing.MplsApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
