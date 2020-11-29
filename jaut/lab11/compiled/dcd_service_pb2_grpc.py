import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2
import dcd_service_pb2 as dcd__service__pb2


class InterfacesServiceStub(object):
  """
  #############################################################

  ***************************************************
  List of interface related config commands 
  **************************************************

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InterfaceCreate = channel.unary_unary(
        '/interface.InterfacesService/InterfaceCreate',
        request_serializer=dcd__service__pb2.InterfaceConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceDelete = channel.unary_unary(
        '/interface.InterfacesService/InterfaceDelete',
        request_serializer=dcd__service__pb2.InterfaceConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceLogicalCreate = channel.unary_unary(
        '/interface.InterfacesService/InterfaceLogicalCreate',
        request_serializer=dcd__service__pb2.InterfaceLogicalConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceLogicalDelete = channel.unary_unary(
        '/interface.InterfacesService/InterfaceLogicalDelete',
        request_serializer=dcd__service__pb2.InterfaceLogicalConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceFamilyCreate = channel.unary_unary(
        '/interface.InterfacesService/InterfaceFamilyCreate',
        request_serializer=dcd__service__pb2.InterfaceFamilyConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceFamilyDelete = channel.unary_unary(
        '/interface.InterfacesService/InterfaceFamilyDelete',
        request_serializer=dcd__service__pb2.InterfaceFamilyConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceAddressCreate = channel.unary_unary(
        '/interface.InterfacesService/InterfaceAddressCreate',
        request_serializer=dcd__service__pb2.InterfaceAddressConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceAddressDelete = channel.unary_unary(
        '/interface.InterfacesService/InterfaceAddressDelete',
        request_serializer=dcd__service__pb2.InterfaceAddressConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceRTAddressCreate = channel.unary_unary(
        '/interface.InterfacesService/InterfaceRTAddressCreate',
        request_serializer=dcd__service__pb2.RTConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )
    self.InterfaceRTAddressDelete = channel.unary_unary(
        '/interface.InterfacesService/InterfaceRTAddressDelete',
        request_serializer=dcd__service__pb2.RTConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.ConfigResp.FromString,
        )


class InterfacesServiceServicer(object):
  """
  #############################################################

  ***************************************************
  List of interface related config commands 
  **************************************************

  """

  def InterfaceCreate(self, request, context):
    """Ifd configuration 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceDelete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceLogicalCreate(self, request, context):
    """Ifl configuration 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceLogicalDelete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceFamilyCreate(self, request, context):
    """IFF configuration 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceFamilyDelete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceAddressCreate(self, request, context):
    """IP address setting for interfaces 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceAddressDelete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceRTAddressCreate(self, request, context):
    """RT address setting for interfaces 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InterfaceRTAddressDelete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InterfacesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InterfaceCreate': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceCreate,
          request_deserializer=dcd__service__pb2.InterfaceConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceDelete': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceDelete,
          request_deserializer=dcd__service__pb2.InterfaceConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceLogicalCreate': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceLogicalCreate,
          request_deserializer=dcd__service__pb2.InterfaceLogicalConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceLogicalDelete': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceLogicalDelete,
          request_deserializer=dcd__service__pb2.InterfaceLogicalConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceFamilyCreate': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceFamilyCreate,
          request_deserializer=dcd__service__pb2.InterfaceFamilyConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceFamilyDelete': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceFamilyDelete,
          request_deserializer=dcd__service__pb2.InterfaceFamilyConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceAddressCreate': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceAddressCreate,
          request_deserializer=dcd__service__pb2.InterfaceAddressConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceAddressDelete': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceAddressDelete,
          request_deserializer=dcd__service__pb2.InterfaceAddressConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceRTAddressCreate': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceRTAddressCreate,
          request_deserializer=dcd__service__pb2.RTConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
      'InterfaceRTAddressDelete': grpc.unary_unary_rpc_method_handler(
          servicer.InterfaceRTAddressDelete,
          request_deserializer=dcd__service__pb2.RTConfig.FromString,
          response_serializer=dcd__service__pb2.ConfigResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interface.InterfacesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AttrQueryServiceStub(object):
  """***************************************************
  List of interface attribute related query commands 
  **************************************************

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InterfacesQueryAttribute = channel.unary_unary(
        '/interface.AttrQueryService/InterfacesQueryAttribute',
        request_serializer=dcd__service__pb2.AttributeRequestInfo.SerializeToString,
        response_deserializer=dcd__service__pb2.AttributeResponseInfo.FromString,
        )


class AttrQueryServiceServicer(object):
  """***************************************************
  List of interface attribute related query commands 
  **************************************************

  """

  def InterfacesQueryAttribute(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AttrQueryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InterfacesQueryAttribute': grpc.unary_unary_rpc_method_handler(
          servicer.InterfacesQueryAttribute,
          request_deserializer=dcd__service__pb2.AttributeRequestInfo.FromString,
          response_serializer=dcd__service__pb2.AttributeResponseInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interface.AttrQueryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ObjectQueryServiceStub(object):
  """***************************************************
  List of object ownership related query commands 
  **************************************************

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.isObjectOwner = channel.unary_unary(
        '/interface.ObjectQueryService/isObjectOwner',
        request_serializer=dcd__service__pb2.ObjectOwnershipQuery.SerializeToString,
        response_deserializer=dcd__service__pb2.ObjectOwnershipResp.FromString,
        )


class ObjectQueryServiceServicer(object):
  """***************************************************
  List of object ownership related query commands 
  **************************************************

  """

  def isObjectOwner(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ObjectQueryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'isObjectOwner': grpc.unary_unary_rpc_method_handler(
          servicer.isObjectOwner,
          request_deserializer=dcd__service__pb2.ObjectOwnershipQuery.FromString,
          response_serializer=dcd__service__pb2.ObjectOwnershipResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interface.ObjectQueryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class TimeoutServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.setClientTimeout = channel.unary_unary(
        '/interface.TimeoutService/setClientTimeout',
        request_serializer=dcd__service__pb2.TimeoutInfo.SerializeToString,
        response_deserializer=dcd__service__pb2.TimeoutResp.FromString,
        )


class TimeoutServiceServicer(object):

  def setClientTimeout(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TimeoutServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'setClientTimeout': grpc.unary_unary_rpc_method_handler(
          servicer.setClientTimeout,
          request_deserializer=dcd__service__pb2.TimeoutInfo.FromString,
          response_serializer=dcd__service__pb2.TimeoutResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interface.TimeoutService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PublicIflServiceStub(object):
  """***************************************************
  List of Public IFL query  commands              *
  **************************************************

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.isPublicIfl = channel.unary_unary(
        '/interface.PublicIflService/isPublicIfl',
        request_serializer=dcd__service__pb2.InterfaceLogicalConfig.SerializeToString,
        response_deserializer=dcd__service__pb2.PublicIflResp.FromString,
        )


class PublicIflServiceServicer(object):
  """***************************************************
  List of Public IFL query  commands              *
  **************************************************

  """

  def isPublicIfl(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublicIflServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'isPublicIfl': grpc.unary_unary_rpc_method_handler(
          servicer.isPublicIfl,
          request_deserializer=dcd__service__pb2.InterfaceLogicalConfig.FromString,
          response_serializer=dcd__service__pb2.PublicIflResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interface.PublicIflService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
