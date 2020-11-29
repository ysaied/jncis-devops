# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pbj.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pbj.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\tpbj.proto\x1a google/protobuf/descriptor.proto\"\xc6\x01\n\nPBJOptions\x12\x10\n\x08max_size\x18\x01 \x01(\x05\x12\x11\n\tmax_count\x18\x02 \x01(\x05\x12$\n\x04type\x18\x03 \x01(\x0e\x32\n.FieldType:\nFT_DEFAULT\x12\x18\n\nlong_names\x18\x04 \x01(\x08:\x04true\x12\x1c\n\rpacked_struct\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cskip_message\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x18\n\ncache_size\x18\x07 \x01(\x08:\x04true*Z\n\tFieldType\x12\x0e\n\nFT_DEFAULT\x10\x00\x12\x0f\n\x0b\x46T_CALLBACK\x10\x01\x12\x0e\n\nFT_POINTER\x10\x04\x12\r\n\tFT_STATIC\x10\x02\x12\r\n\tFT_IGNORE\x10\x03:C\n\x0fpbj_file_option\x12\x1c.google.protobuf.FileOptions\x18\xfc\x07 \x01(\x0b\x32\x0b.PBJOptions:I\n\x12pbj_message_option\x12\x1f.google.protobuf.MessageOptions\x18\xfc\x07 \x01(\x0b\x32\x0b.PBJOptions:C\n\x0fpbj_enum_option\x12\x1c.google.protobuf.EnumOptions\x18\xfc\x07 \x01(\x0b\x32\x0b.PBJOptions:E\n\x10pbj_field_option\x12\x1d.google.protobuf.FieldOptions\x18\xfc\x07 \x01(\x0b\x32\x0b.PBJOptionsB\x11\n\x0fnet.juniper.pbj')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='FieldType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FT_DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_CALLBACK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_POINTER', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_STATIC', index=3, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FT_IGNORE', index=4, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=248,
  serialized_end=338,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE)

FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
FT_DEFAULT = 0
FT_CALLBACK = 1
FT_POINTER = 4
FT_STATIC = 2
FT_IGNORE = 3

PBJ_FILE_OPTION_FIELD_NUMBER = 1020
pbj_file_option = _descriptor.FieldDescriptor(
  name='pbj_file_option', full_name='pbj_file_option', index=0,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
PBJ_MESSAGE_OPTION_FIELD_NUMBER = 1020
pbj_message_option = _descriptor.FieldDescriptor(
  name='pbj_message_option', full_name='pbj_message_option', index=1,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
PBJ_ENUM_OPTION_FIELD_NUMBER = 1020
pbj_enum_option = _descriptor.FieldDescriptor(
  name='pbj_enum_option', full_name='pbj_enum_option', index=2,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
PBJ_FIELD_OPTION_FIELD_NUMBER = 1020
pbj_field_option = _descriptor.FieldDescriptor(
  name='pbj_field_option', full_name='pbj_field_option', index=3,
  number=1020, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_PBJOPTIONS = _descriptor.Descriptor(
  name='PBJOptions',
  full_name='PBJOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_size', full_name='PBJOptions.max_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_count', full_name='PBJOptions.max_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='PBJOptions.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long_names', full_name='PBJOptions.long_names', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='packed_struct', full_name='PBJOptions.packed_struct', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skip_message', full_name='PBJOptions.skip_message', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cache_size', full_name='PBJOptions.cache_size', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=48,
  serialized_end=246,
)

_PBJOPTIONS.fields_by_name['type'].enum_type = _FIELDTYPE
DESCRIPTOR.message_types_by_name['PBJOptions'] = _PBJOPTIONS
DESCRIPTOR.enum_types_by_name['FieldType'] = _FIELDTYPE
DESCRIPTOR.extensions_by_name['pbj_file_option'] = pbj_file_option
DESCRIPTOR.extensions_by_name['pbj_message_option'] = pbj_message_option
DESCRIPTOR.extensions_by_name['pbj_enum_option'] = pbj_enum_option
DESCRIPTOR.extensions_by_name['pbj_field_option'] = pbj_field_option

PBJOptions = _reflection.GeneratedProtocolMessageType('PBJOptions', (_message.Message,), dict(
  DESCRIPTOR = _PBJOPTIONS,
  __module__ = 'pbj_pb2'
  # @@protoc_insertion_point(class_scope:PBJOptions)
  ))
_sym_db.RegisterMessage(PBJOptions)

pbj_file_option.message_type = _PBJOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(pbj_file_option)
pbj_message_option.message_type = _PBJOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(pbj_message_option)
pbj_enum_option.message_type = _PBJOPTIONS
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(pbj_enum_option)
pbj_field_option.message_type = _PBJOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(pbj_field_option)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\017net.juniper.pbj'))
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
