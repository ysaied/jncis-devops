# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cpu_memory_utilization.proto

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
  name='cpu_memory_utilization.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x63pu_memory_utilization.proto\x1a\x13telemetry_top.proto\"I\n\x14\x43puMemoryUtilization\x12\x31\n\x0butilization\x18\x01 \x03(\x0b\x32\x1c.CpuMemoryUtilizationSummary\"\xad\x01\n\x1b\x43puMemoryUtilizationSummary\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x17\n\x0f\x62ytes_allocated\x18\x03 \x01(\x04\x12\x13\n\x0butilization\x18\x04 \x01(\x05\x12\x44\n\x17\x61pplication_utilization\x18\x05 \x03(\x0b\x32#.CpuMemoryUtilizationPerApplication\"\x8b\x01\n\"CpuMemoryUtilizationPerApplication\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x62ytes_allocated\x18\x02 \x01(\x04\x12\x13\n\x0b\x61llocations\x18\x03 \x01(\x04\x12\r\n\x05\x66rees\x18\x04 \x01(\x04\x12\x1a\n\x12\x61llocations_failed\x18\x05 \x01(\x04:K\n\x13\x63pu_memory_util_ext\x12\x17.JuniperNetworksSensors\x18\x01 \x01(\x0b\x32\x15.CpuMemoryUtilization')
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


CPU_MEMORY_UTIL_EXT_FIELD_NUMBER = 1
cpu_memory_util_ext = _descriptor.FieldDescriptor(
  name='cpu_memory_util_ext', full_name='cpu_memory_util_ext', index=0,
  number=1, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_CPUMEMORYUTILIZATION = _descriptor.Descriptor(
  name='CpuMemoryUtilization',
  full_name='CpuMemoryUtilization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utilization', full_name='CpuMemoryUtilization.utilization', index=0,
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
  serialized_end=126,
)


_CPUMEMORYUTILIZATIONSUMMARY = _descriptor.Descriptor(
  name='CpuMemoryUtilizationSummary',
  full_name='CpuMemoryUtilizationSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CpuMemoryUtilizationSummary.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='CpuMemoryUtilizationSummary.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_allocated', full_name='CpuMemoryUtilizationSummary.bytes_allocated', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utilization', full_name='CpuMemoryUtilizationSummary.utilization', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='application_utilization', full_name='CpuMemoryUtilizationSummary.application_utilization', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=129,
  serialized_end=302,
)


_CPUMEMORYUTILIZATIONPERAPPLICATION = _descriptor.Descriptor(
  name='CpuMemoryUtilizationPerApplication',
  full_name='CpuMemoryUtilizationPerApplication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CpuMemoryUtilizationPerApplication.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_allocated', full_name='CpuMemoryUtilizationPerApplication.bytes_allocated', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocations', full_name='CpuMemoryUtilizationPerApplication.allocations', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frees', full_name='CpuMemoryUtilizationPerApplication.frees', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocations_failed', full_name='CpuMemoryUtilizationPerApplication.allocations_failed', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=305,
  serialized_end=444,
)

_CPUMEMORYUTILIZATION.fields_by_name['utilization'].message_type = _CPUMEMORYUTILIZATIONSUMMARY
_CPUMEMORYUTILIZATIONSUMMARY.fields_by_name['application_utilization'].message_type = _CPUMEMORYUTILIZATIONPERAPPLICATION
DESCRIPTOR.message_types_by_name['CpuMemoryUtilization'] = _CPUMEMORYUTILIZATION
DESCRIPTOR.message_types_by_name['CpuMemoryUtilizationSummary'] = _CPUMEMORYUTILIZATIONSUMMARY
DESCRIPTOR.message_types_by_name['CpuMemoryUtilizationPerApplication'] = _CPUMEMORYUTILIZATIONPERAPPLICATION
DESCRIPTOR.extensions_by_name['cpu_memory_util_ext'] = cpu_memory_util_ext

CpuMemoryUtilization = _reflection.GeneratedProtocolMessageType('CpuMemoryUtilization', (_message.Message,), dict(
  DESCRIPTOR = _CPUMEMORYUTILIZATION,
  __module__ = 'cpu_memory_utilization_pb2'
  # @@protoc_insertion_point(class_scope:CpuMemoryUtilization)
  ))
_sym_db.RegisterMessage(CpuMemoryUtilization)

CpuMemoryUtilizationSummary = _reflection.GeneratedProtocolMessageType('CpuMemoryUtilizationSummary', (_message.Message,), dict(
  DESCRIPTOR = _CPUMEMORYUTILIZATIONSUMMARY,
  __module__ = 'cpu_memory_utilization_pb2'
  # @@protoc_insertion_point(class_scope:CpuMemoryUtilizationSummary)
  ))
_sym_db.RegisterMessage(CpuMemoryUtilizationSummary)

CpuMemoryUtilizationPerApplication = _reflection.GeneratedProtocolMessageType('CpuMemoryUtilizationPerApplication', (_message.Message,), dict(
  DESCRIPTOR = _CPUMEMORYUTILIZATIONPERAPPLICATION,
  __module__ = 'cpu_memory_utilization_pb2'
  # @@protoc_insertion_point(class_scope:CpuMemoryUtilizationPerApplication)
  ))
_sym_db.RegisterMessage(CpuMemoryUtilizationPerApplication)

cpu_memory_util_ext.message_type = _CPUMEMORYUTILIZATION
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(cpu_memory_util_ext)

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