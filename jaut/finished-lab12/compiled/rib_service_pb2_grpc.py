import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2
import rib_service_pb2 as rib__service__pb2


class RibStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RouteAdd = channel.unary_unary(
        '/routing.Rib/RouteAdd',
        request_serializer=rib__service__pb2.RouteUpdateRequest.SerializeToString,
        response_deserializer=rib__service__pb2.RouteOperReply.FromString,
        )
    self.RouteModify = channel.unary_unary(
        '/routing.Rib/RouteModify',
        request_serializer=rib__service__pb2.RouteUpdateRequest.SerializeToString,
        response_deserializer=rib__service__pb2.RouteOperReply.FromString,
        )
    self.RouteUpdate = channel.unary_unary(
        '/routing.Rib/RouteUpdate',
        request_serializer=rib__service__pb2.RouteUpdateRequest.SerializeToString,
        response_deserializer=rib__service__pb2.RouteOperReply.FromString,
        )
    self.RouteRemove = channel.unary_unary(
        '/routing.Rib/RouteRemove',
        request_serializer=rib__service__pb2.RouteRemoveRequest.SerializeToString,
        response_deserializer=rib__service__pb2.RouteOperReply.FromString,
        )
    self.RouteGet = channel.unary_stream(
        '/routing.Rib/RouteGet',
        request_serializer=rib__service__pb2.RouteGetRequest.SerializeToString,
        response_deserializer=rib__service__pb2.RouteGetReply.FromString,
        )
    self.RouteMonitorRegister = channel.unary_stream(
        '/routing.Rib/RouteMonitorRegister',
        request_serializer=rib__service__pb2.RouteMonitorRegRequest.SerializeToString,
        response_deserializer=rib__service__pb2.RouteMonitorReply.FromString,
        )


class RibServicer(object):

  def RouteAdd(self, request, context):
    """* Route Add operation

    Add a static route to the routing table.

    RouteAdd may be called multiple times for the same prefix to add
    multiple paths with distinct cookie for the same destination.
    If a matching route already exists in the given table, then an error
    will be returned.

    RoutingRouteOperRequest may contain from one to 1000 routes to be added.

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

  def RouteModify(self, request, context):
    """* Route Modify operation
    Modify an existing programmed static route in the routing table. For
    each route in the request, if the key is matched, the matched route will
    be updated with the supplied route attributes.

    If a matching route does not exist in the given table, then an error
    will be returned.

    RouteUpdateRequest may contain from one to 1000 routes to be added.
    If the request contains multiple routes, the routes will be processed
    in the order given and the first error encountered will cause the
    request to abort.
    The API always returns the final status (success or first error
    encountered) and the number of routes that were successfully modified
    prior to any error or full completion of the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RouteUpdate(self, request, context):
    """* Route Update operation
    Create a new static route if a matching route does not exist, OR
    modify an existing static route if it is already present in the
    routing table.
    RouteUpdateRequest may contain from one to 1000 routes to be added.
    If the request contains multiple routes, the routes will be processed
    in the order given and the first error encountered will cause the
    request to abort.
    The API always returns the final status (success or first error
    encountered) and the number of routes that were successfully modified
    prior to any error or full completion of the request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RouteRemove(self, request, context):
    """* Route Remove operation

    Remove a static route from the routing table.
    RouteRemove may be called multiple times for the same prefix
    to remove multiple paths with distinct path_cookie for the same
    destination. (NOTE: cookie support not yet implemented)

    The request may contain from one to 1000 routes  to be removed.

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

  def RouteGet(self, request, context):
    """* Route Get operation
    Lookup a route from the routing table.
    All match parameters are optional.
    Match fields that are not specified or that
    may match more than one route (e.g. a less-specific destination
    prefix) may result in multiple routes being returned in the replies.

    Responses are bulked for performance and the client can specify
    maxmimum number of route entries that JUNOS can send in one response
    message using route_count field. JUNOS may chose to pack less
    number of entries than that client has specified.

    Multiple route entries matching matching a given route prefix
    may be be counted as one (if its last one in the response) and may
    result in exceeding the specified route count.

    Replies are streamed until all match routes have been sent. The
    client will receive a final null message once all routes have
    been received.
    The server's walk of search results is not atomic so route changes
    during streaming and consumption of replies may or may not be
    reflected in the results.
    See RouteGetReply.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RouteMonitorRegister(self, request, context):
    """*
    Register for route monitoring to monitor the route entries of a table.
    When clients register for a table all routes that passes policy are
    streamed to the client. After this the routes that get added or changed
    or deleted are streamed.

    Clients can register to more than one table for route monitoring. Each
    of these registrations will have a different stream on which the routes
    will be streamed. 

    Clients can also change registration parameters for the table. In this
    case the parameter will be re-applied for the table and the resulting
    routes of the table are streamed. For e.g if policy is added to the
    registration to noitfy only static routes, then all non static routes 
    that were sent before are re-sent with a delete monitor operation. 
    Subsequent monitor messages for the table will contain only static
    routes. 
    For the above case, streaming will happen on the new stream created for
    the fresh Register request sent. Streaming of routes on the old stream
    will stop.

    The reply is sent as stream and will be sent as long as monitor 
    registration is valid. Once the monitor registration is deleted, 
    then this streaming will be stopped.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RibServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RouteAdd': grpc.unary_unary_rpc_method_handler(
          servicer.RouteAdd,
          request_deserializer=rib__service__pb2.RouteUpdateRequest.FromString,
          response_serializer=rib__service__pb2.RouteOperReply.SerializeToString,
      ),
      'RouteModify': grpc.unary_unary_rpc_method_handler(
          servicer.RouteModify,
          request_deserializer=rib__service__pb2.RouteUpdateRequest.FromString,
          response_serializer=rib__service__pb2.RouteOperReply.SerializeToString,
      ),
      'RouteUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.RouteUpdate,
          request_deserializer=rib__service__pb2.RouteUpdateRequest.FromString,
          response_serializer=rib__service__pb2.RouteOperReply.SerializeToString,
      ),
      'RouteRemove': grpc.unary_unary_rpc_method_handler(
          servicer.RouteRemove,
          request_deserializer=rib__service__pb2.RouteRemoveRequest.FromString,
          response_serializer=rib__service__pb2.RouteOperReply.SerializeToString,
      ),
      'RouteGet': grpc.unary_stream_rpc_method_handler(
          servicer.RouteGet,
          request_deserializer=rib__service__pb2.RouteGetRequest.FromString,
          response_serializer=rib__service__pb2.RouteGetReply.SerializeToString,
      ),
      'RouteMonitorRegister': grpc.unary_stream_rpc_method_handler(
          servicer.RouteMonitorRegister,
          request_deserializer=rib__service__pb2.RouteMonitorRegRequest.FromString,
          response_serializer=rib__service__pb2.RouteMonitorReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'routing.Rib', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
