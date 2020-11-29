# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sr_stats_per_if_egress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import telemetry_top_pb2 as telemetry__top__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sr_stats_per_if_egress.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1csr_stats_per_if_egress.proto\x1a\x13telemetry_top.proto\"L\n\x12SrStatsPerIfEgress\x12\x36\n\x0eper_if_records\x18\x01 \x03(\x0b\x32\x1e.SegmentRoutingInterfaceRecord\"\xd0\x01\n\x1dSegmentRoutingInterfaceRecord\x12\x16\n\x07if_name\x18\x01 \x02(\tB\x05\x82@\x02\x08\x01\x12\x1d\n\x0eparent_ae_name\x18\x02 \x01(\tB\x05\x82@\x02\x08\x01\x12\x1b\n\x0c\x63ounter_name\x18\x03 \x01(\tB\x05\x82@\x02\x08\x01\x12-\n\ringress_stats\x18\x04 \x01(\x0b\x32\x16.SegmentRoutingIfStats\x12,\n\x0c\x65gress_stats\x18\x05 \x01(\x0b\x32\x16.SegmentRoutingIfStats\"{\n\x15SegmentRoutingIfStats\x12\x16\n\x07packets\x18\x01 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x14\n\x05\x62ytes\x18\x02 \x01(\x04\x42\x05\x82@\x02\x18\x01\x12\x1a\n\x0bpacket_rate\x18\x03 \x01(\x04\x42\x05\x82@\x02 \x01\x12\x18\n\tbyte_rate\x18\x04 \x01(\x04\x42\x05\x82@\x02 \x01:U\n\x1fjnpr_sr_stats_per_if_egress_ext\x12\x17.JuniperNetworksSensors\x18\x11 \x01(\x0b\x32\x13.SrStatsPerIfEgress')
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


JNPR_SR_STATS_PER_IF_EGRESS_EXT_FIELD_NUMBER = 17
jnpr_sr_stats_per_if_egress_ext = _descriptor.FieldDescriptor(
  name='jnpr_sr_stats_per_if_egress_ext', full_name='jnpr_sr_stats_per_if_egress_ext', index=0,
  number=17, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_SRSTATSPERIFEGRESS = _descriptor.Descriptor(
  name='SrStatsPerIfEgress',
  full_name='SrStatsPerIfEgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='per_if_records', full_name='SrStatsPerIfEgress.per_if_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=129,
)


_SEGMENTROUTINGINTERFACERECORD = _descriptor.Descriptor(
  name='SegmentRoutingInterfaceRecord',
  full_name='SegmentRoutingInterfaceRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_name', full_name='SegmentRoutingInterfaceRecord.if_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='parent_ae_name', full_name='SegmentRoutingInterfaceRecord.parent_ae_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='counter_name', full_name='SegmentRoutingInterfaceRecord.counter_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='ingress_stats', full_name='SegmentRoutingInterfaceRecord.ingress_stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_stats', full_name='SegmentRoutingInterfaceRecord.egress_stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=340,
)


_SEGMENTROUTINGIFSTATS = _descriptor.Descriptor(
  name='SegmentRoutingIfStats',
  full_name='SegmentRoutingIfStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packets', full_name='SegmentRoutingIfStats.packets', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\030\001'))),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='SegmentRoutingIfStats.bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\030\001'))),
    _descriptor.FieldDescriptor(
      name='packet_rate', full_name='SegmentRoutingIfStats.packet_rate', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002 \001'))),
    _descriptor.FieldDescriptor(
      name='byte_rate', full_name='SegmentRoutingIfStats.byte_rate', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002 \001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=465,
)

_SRSTATSPERIFEGRESS.fields_by_name['per_if_records'].message_type = _SEGMENTROUTINGINTERFACERECORD
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['ingress_stats'].message_type = _SEGMENTROUTINGIFSTATS
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['egress_stats'].message_type = _SEGMENTROUTINGIFSTATS
DESCRIPTOR.message_types_by_name['SrStatsPerIfEgress'] = _SRSTATSPERIFEGRESS
DESCRIPTOR.message_types_by_name['SegmentRoutingInterfaceRecord'] = _SEGMENTROUTINGINTERFACERECORD
DESCRIPTOR.message_types_by_name['SegmentRoutingIfStats'] = _SEGMENTROUTINGIFSTATS
DESCRIPTOR.extensions_by_name['jnpr_sr_stats_per_if_egress_ext'] = jnpr_sr_stats_per_if_egress_ext

SrStatsPerIfEgress = _reflection.GeneratedProtocolMessageType('SrStatsPerIfEgress', (_message.Message,), dict(
  DESCRIPTOR = _SRSTATSPERIFEGRESS,
  __module__ = 'sr_stats_per_if_egress_pb2'
  # @@protoc_insertion_point(class_scope:SrStatsPerIfEgress)
  ))
_sym_db.RegisterMessage(SrStatsPerIfEgress)

SegmentRoutingInterfaceRecord = _reflection.GeneratedProtocolMessageType('SegmentRoutingInterfaceRecord', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENTROUTINGINTERFACERECORD,
  __module__ = 'sr_stats_per_if_egress_pb2'
  # @@protoc_insertion_point(class_scope:SegmentRoutingInterfaceRecord)
  ))
_sym_db.RegisterMessage(SegmentRoutingInterfaceRecord)

SegmentRoutingIfStats = _reflection.GeneratedProtocolMessageType('SegmentRoutingIfStats', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENTROUTINGIFSTATS,
  __module__ = 'sr_stats_per_if_egress_pb2'
  # @@protoc_insertion_point(class_scope:SegmentRoutingIfStats)
  ))
_sym_db.RegisterMessage(SegmentRoutingIfStats)

jnpr_sr_stats_per_if_egress_ext.message_type = _SRSTATSPERIFEGRESS
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(jnpr_sr_stats_per_if_egress_ext)

_SEGMENTROUTINGINTERFACERECORD.fields_by_name['if_name'].has_options = True
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['if_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['parent_ae_name'].has_options = True
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['parent_ae_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['counter_name'].has_options = True
_SEGMENTROUTINGINTERFACERECORD.fields_by_name['counter_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))
_SEGMENTROUTINGIFSTATS.fields_by_name['packets'].has_options = True
_SEGMENTROUTINGIFSTATS.fields_by_name['packets']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\030\001'))
_SEGMENTROUTINGIFSTATS.fields_by_name['bytes'].has_options = True
_SEGMENTROUTINGIFSTATS.fields_by_name['bytes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\030\001'))
_SEGMENTROUTINGIFSTATS.fields_by_name['packet_rate'].has_options = True
_SEGMENTROUTINGIFSTATS.fields_by_name['packet_rate']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002 \001'))
_SEGMENTROUTINGIFSTATS.fields_by_name['byte_rate'].has_options = True
_SEGMENTROUTINGIFSTATS.fields_by_name['byte_rate']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002 \001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
