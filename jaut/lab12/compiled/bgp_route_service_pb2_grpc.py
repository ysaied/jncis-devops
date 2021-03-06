import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2
import bgp_route_service_pb2 as bgp__route__service__pb2


class BgpRouteStub(object):
  """*
  BGP route operations service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.BgpRouteInitialize = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteInitialize',
        request_serializer=bgp__route__service__pb2.BgpRouteInitializeRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteInitializeReply.FromString,
        )
    self.BgpRouteCleanup = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteCleanup',
        request_serializer=bgp__route__service__pb2.BgpRouteCleanupRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteCleanupReply.FromString,
        )
    self.BgpRouteAdd = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteAdd',
        request_serializer=bgp__route__service__pb2.BgpRouteUpdateRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteOperReply.FromString,
        )
    self.BgpRouteModify = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteModify',
        request_serializer=bgp__route__service__pb2.BgpRouteUpdateRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteOperReply.FromString,
        )
    self.BgpRouteUpdate = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteUpdate',
        request_serializer=bgp__route__service__pb2.BgpRouteUpdateRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteOperReply.FromString,
        )
    self.BgpRouteRemove = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteRemove',
        request_serializer=bgp__route__service__pb2.BgpRouteRemoveRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteOperReply.FromString,
        )
    self.BgpRouteGet = channel.unary_stream(
        '/routing.BgpRoute/BgpRouteGet',
        request_serializer=bgp__route__service__pb2.BgpRouteGetRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteGetReply.FromString,
        )
    self.BgpRouteMonitorRegister = channel.unary_stream(
        '/routing.BgpRoute/BgpRouteMonitorRegister',
        request_serializer=bgp__route__service__pb2.BgpRouteMonitorRegisterRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteMonitorRegisterReply.FromString,
        )
    self.BgpRouteMonitorUnregister = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteMonitorUnregister',
        request_serializer=bgp__route__service__pb2.BgpRouteMonitorUnregisterRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteMonitorUnregisterReply.FromString,
        )
    self.BgpRouteMonitorRefresh = channel.unary_unary(
        '/routing.BgpRoute/BgpRouteMonitorRefresh',
        request_serializer=bgp__route__service__pb2.BgpRouteMonitorRefreshRequest.SerializeToString,
        response_deserializer=bgp__route__service__pb2.BgpRouteMonitorRefreshReply.FromString,
        )


class BgpRouteServicer(object):
  """*
  BGP route operations service
  """

  def BgpRouteInitialize(self, request, context):
    """* BGP Routing Initialize operation
    BgpRouteInitialize() must be called upon connection or reconnection
    to the server. If the client is connecting for the first time, the
    server will initialize per-client state for the connection.
    If the client is reconnecting with the same client name following a 
    connection fault (having not closed a previous connection with
    BgpRouteCleanup), then gateway and route state will be rebound to 
    the new connection.
    In this case, the return status will indicate that state was rebound
    and the client need not reply the previous routing state to the 
    server. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteCleanup(self, request, context):
    """* BGP Routing Cleanup operation
    BgpRouteCleanup will purge all gateway and route state for the
    client. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteAdd(self, request, context):
    """* BGP Route Add operation
    Add a BGP-Static route to the routing table.
    bgp_route_add may be called multiple times for the same prefix to add 
    multiple paths with distinct path_cookie for the same destination. 
    If a matching route already exists in the given table, then an error
    will be returned.
    BgpRouteUpdateRequest may contain from one to 1000 routes
    to be added. 
    If the request contains multiple routes, the routes will
    be processed in the order given and the first error encountered will
    cause the request to abort.
    The API always returns the final status (success or first error
    encountered) and the number of routes that were successfully created 
    prior to any error or full completion of the request. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteModify(self, request, context):
    """* BGP Route Modify operation
    Modify an existing BGP-Static route in the routing table. For each
    route in the request, if the route_key is matched, the matched route
    will be updated with the supplied route attributes.
    If a matching route does not exist in the given table, then an error
    will be returned.
    BgpRouteUpdateRequest may contain from one to 1000 routes
    to be added. 
    If the request contains multiple routes, the routes will
    be processed in the order given and the first error encountered will
    cause the request to abort.
    The API always returns the final status (success or first error
    encountered) and the number of routes that were successfully modified
    prior to any error or full completion of the request. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteUpdate(self, request, context):
    """* BGP Route Update operation
    Create a new BGP-Static route if a matching route does not exist, OR
    modify an existing BGP-Static route if it is already present in the
    routing table. 
    BgpRouteUpdateRequest may contain from one to 1000 routes
    to be added. 
    If the request contains multiple routes, the routes will
    be processed in the order given and the first error encountered will
    cause the request to abort.
    The API always returns the final status (success or first error
    encountered) and the number of routes that were successfully modified
    prior to any error or full completion of the request. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteRemove(self, request, context):
    """* BGP Route Remove operation
    Remove a BGP-Static route from the routing table.
    BgpRouteRemove may be called multiple times for the same prefix 
    to remove multiple paths with distinct path_cookie for the same 
    destination. 
    The request may contain from one to 1000 routes
    to be removed.
    If the request contains multiple routes, the routes will
    be processed in the order given and the first error encountered will
    cause the request to abort.
    The API always returns the final status (success or first error
    encountered) and the number of routes that were successfully modified
    prior to any error or full completion of the request. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteGet(self, request, context):
    """* BGP Route Get operation
    Lookup a BGP or BGP-Static protocol route from the routing table.
    All match parameters are optional.
    Match fields that are not specified or that
    may match more than one route (e.g. a less-specific destination 
    prefix) may result in multiple routes being returned in the replies.
    Only BGP and BGP-Static routes will be matched.
    Replies are streamed until all match routes have been sent. The
    client will receive a final null message once all routes have 
    been received.
    The server's walk of search results is not atomic so route changes
    during streaming and consumption of replies may or may not be 
    reflected in the results.
    See BgpRouteGetReply. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteMonitorRegister(self, request, context):
    """* 
    BGP Route Monitoring Registration
    Register to receive updates streamed from BGP when routes matching
    the bgp-import "analyze" policy action are added, modified, or 
    withdrawn by BGP peers.
    Updates will be streamed as BgpRouteMonitorRegisterReply mesages
    BgpRouteMonitorUnregister() is called.
    Upon initial registration, a full download of route ADD operations for 
    all routes matching the "analyze" import policy action will be 
    streamed, followed by a closing END_OF_RIB operation. Subsequently,
    incremental updates will be streamed whenever BGP advertisements 
    from peers are added, modified, or withdrawn, or when BGP import 
    "analyze" policy is changed.
    There is no strict ordering of routes in the update stream and
    state compression is applied when applicable to a set of operations. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteMonitorUnregister(self, request, context):
    """* 
    BGP Route Monitoring Unregistration
    Generated client API: BgpRouteMonitorUnregister()
    Unregister to receive updates streamed from BGP when routes are
    added, modified, or withdrawn by BGP peers. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BgpRouteMonitorRefresh(self, request, context):
    """* 
    BGP Route Monitoring Refresh
    Generated client API: BgpRouteMonitorRefresh()
    Request to refresh all route monitoring entries to the client.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BgpRouteServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'BgpRouteInitialize': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteInitialize,
          request_deserializer=bgp__route__service__pb2.BgpRouteInitializeRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteInitializeReply.SerializeToString,
      ),
      'BgpRouteCleanup': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteCleanup,
          request_deserializer=bgp__route__service__pb2.BgpRouteCleanupRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteCleanupReply.SerializeToString,
      ),
      'BgpRouteAdd': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteAdd,
          request_deserializer=bgp__route__service__pb2.BgpRouteUpdateRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteOperReply.SerializeToString,
      ),
      'BgpRouteModify': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteModify,
          request_deserializer=bgp__route__service__pb2.BgpRouteUpdateRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteOperReply.SerializeToString,
      ),
      'BgpRouteUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteUpdate,
          request_deserializer=bgp__route__service__pb2.BgpRouteUpdateRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteOperReply.SerializeToString,
      ),
      'BgpRouteRemove': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteRemove,
          request_deserializer=bgp__route__service__pb2.BgpRouteRemoveRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteOperReply.SerializeToString,
      ),
      'BgpRouteGet': grpc.unary_stream_rpc_method_handler(
          servicer.BgpRouteGet,
          request_deserializer=bgp__route__service__pb2.BgpRouteGetRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteGetReply.SerializeToString,
      ),
      'BgpRouteMonitorRegister': grpc.unary_stream_rpc_method_handler(
          servicer.BgpRouteMonitorRegister,
          request_deserializer=bgp__route__service__pb2.BgpRouteMonitorRegisterRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteMonitorRegisterReply.SerializeToString,
      ),
      'BgpRouteMonitorUnregister': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteMonitorUnregister,
          request_deserializer=bgp__route__service__pb2.BgpRouteMonitorUnregisterRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteMonitorUnregisterReply.SerializeToString,
      ),
      'BgpRouteMonitorRefresh': grpc.unary_unary_rpc_method_handler(
          servicer.BgpRouteMonitorRefresh,
          request_deserializer=bgp__route__service__pb2.BgpRouteMonitorRefreshRequest.FromString,
          response_serializer=bgp__route__service__pb2.BgpRouteMonitorRefreshReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routing.BgpRoute', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
