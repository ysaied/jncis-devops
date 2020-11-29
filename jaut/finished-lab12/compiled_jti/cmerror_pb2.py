# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmerror.proto

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
  name='cmerror.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rcmerror.proto\x1a\x13telemetry_top.proto\"\x98\x03\n\x05\x45rror\x12\x19\n\nidentifier\x18\x01 \x01(\tB\x05\x82@\x02\x08\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x63omponent_id\x18\x03 \x01(\r\x12\x10\n\x08\x66ru_type\x18\x04 \x01(\t\x12\x10\n\x08\x66ru_slot\x18\x05 \x01(\r\x12\r\n\x05scope\x18\x06 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x07 \x01(\t\x12\x10\n\x08severity\x18\x08 \x01(\t\x12\x11\n\tthreshold\x18\t \x01(\r\x12\r\n\x05limit\x18\n \x01(\r\x12\x19\n\x11raising_threshold\x18\x0b \x01(\r\x12\x1a\n\x12\x63learing_threshold\x18\x0c \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\r \x01(\r\x12\x1c\n\x14\x61\x63tion_handling_type\x18\x0e \x01(\r\x12\x1c\n\x14\x63onfigured_threshold\x18\x0f \x01(\r\x12\x18\n\x10\x63onfigured_limit\x18\x10 \x01(\r\x12\x19\n\x11\x63onfigured_action\x18\x11 \x01(\r\x12\x1f\n\x17\x63onfigured_clear_action\x18\x12 \x01(\r\"p\n\x18GlobalErrorConfiguration\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x10\n\x08severity\x18\x03 \x01(\t\x12\x11\n\tthreshold\x18\x04 \x01(\r\x12\x0e\n\x06\x61\x63tion\x18\x05 \x01(\r\"\xc5\x01\n\x07\x43merror\x12\x1a\n\nerror_item\x18\x01 \x03(\x0b\x32\x06.Error\x12!\n\x19last_configuration_change\x18\x02 \x01(\x04\x12\x19\n\x11wrap_cycle_marker\x18\x03 \x01(\x08\x12\x10\n\x08\x66ru_slot\x18\x04 \x01(\r\x12\x10\n\x08\x66ru_type\x18\x05 \x01(\t\x12<\n\x19global_configuration_item\x18\x06 \x03(\x0b\x32\x19.GlobalErrorConfiguration:;\n\x10jnpr_cmerror_ext\x12\x17.JuniperNetworksSensors\x18\x14 \x01(\x0b\x32\x08.Cmerror')
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


JNPR_CMERROR_EXT_FIELD_NUMBER = 20
jnpr_cmerror_ext = _descriptor.FieldDescriptor(
  name='jnpr_cmerror_ext', full_name='jnpr_cmerror_ext', index=0,
  number=20, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='Error.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='name', full_name='Error.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='component_id', full_name='Error.component_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fru_type', full_name='Error.fru_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fru_slot', full_name='Error.fru_slot', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scope', full_name='Error.scope', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='Error.category', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='Error.severity', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='Error.threshold', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='Error.limit', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raising_threshold', full_name='Error.raising_threshold', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clearing_threshold', full_name='Error.clearing_threshold', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='Error.action', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action_handling_type', full_name='Error.action_handling_type', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='configured_threshold', full_name='Error.configured_threshold', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='configured_limit', full_name='Error.configured_limit', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='configured_action', full_name='Error.configured_action', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='configured_clear_action', full_name='Error.configured_clear_action', index=17,
      number=18, type=13, cpp_type=3, label=1,
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
  serialized_start=39,
  serialized_end=447,
)


_GLOBALERRORCONFIGURATION = _descriptor.Descriptor(
  name='GlobalErrorConfiguration',
  full_name='GlobalErrorConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scope', full_name='GlobalErrorConfiguration.scope', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='GlobalErrorConfiguration.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='GlobalErrorConfiguration.severity', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='GlobalErrorConfiguration.threshold', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='GlobalErrorConfiguration.action', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=449,
  serialized_end=561,
)


_CMERROR = _descriptor.Descriptor(
  name='Cmerror',
  full_name='Cmerror',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_item', full_name='Cmerror.error_item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_configuration_change', full_name='Cmerror.last_configuration_change', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wrap_cycle_marker', full_name='Cmerror.wrap_cycle_marker', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fru_slot', full_name='Cmerror.fru_slot', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fru_type', full_name='Cmerror.fru_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='global_configuration_item', full_name='Cmerror.global_configuration_item', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=564,
  serialized_end=761,
)

_CMERROR.fields_by_name['error_item'].message_type = _ERROR
_CMERROR.fields_by_name['global_configuration_item'].message_type = _GLOBALERRORCONFIGURATION
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['GlobalErrorConfiguration'] = _GLOBALERRORCONFIGURATION
DESCRIPTOR.message_types_by_name['Cmerror'] = _CMERROR
DESCRIPTOR.extensions_by_name['jnpr_cmerror_ext'] = jnpr_cmerror_ext

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'cmerror_pb2'
  # @@protoc_insertion_point(class_scope:Error)
  ))
_sym_db.RegisterMessage(Error)

GlobalErrorConfiguration = _reflection.GeneratedProtocolMessageType('GlobalErrorConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALERRORCONFIGURATION,
  __module__ = 'cmerror_pb2'
  # @@protoc_insertion_point(class_scope:GlobalErrorConfiguration)
  ))
_sym_db.RegisterMessage(GlobalErrorConfiguration)

Cmerror = _reflection.GeneratedProtocolMessageType('Cmerror', (_message.Message,), dict(
  DESCRIPTOR = _CMERROR,
  __module__ = 'cmerror_pb2'
  # @@protoc_insertion_point(class_scope:Cmerror)
  ))
_sym_db.RegisterMessage(Cmerror)

jnpr_cmerror_ext.message_type = _CMERROR
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(jnpr_cmerror_ext)

_ERROR.fields_by_name['identifier'].has_options = True
_ERROR.fields_by_name['identifier']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202@\002\010\001'))
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
