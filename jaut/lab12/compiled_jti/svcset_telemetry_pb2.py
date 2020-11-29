# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: svcset_telemetry.proto

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
  name='svcset_telemetry.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16svcset_telemetry.proto\x1a\x13telemetry_top.proto\"\xdb\x01\n\rServicesInfra\x12\'\n\x11svcs_plugins_info\x18\x01 \x03(\x0b\x32\x0c.PluginsInfo\x12&\n\x0fsvcset_cpu_info\x18\x02 \x03(\x0b\x32\r.CpuUsageInfo\x12&\n\x0fsvcset_mem_info\x18\x03 \x03(\x0b\x32\r.MemUsageInfo\x12&\n\x0fsvcset_svc_info\x18\x04 \x03(\x0b\x32\r.ServicesInfo\x12)\n\x13svcset_pktdrop_info\x18\x05 \x03(\x0b\x32\x0c.PktDropInfo\"\xb3\x02\n\x0bPluginsInfo\x12\x16\n\x0esp_num_plugins\x18\x01 \x01(\x04\x12\x0f\n\x07sp_name\x18\x02 \x01(\t\x12\x0e\n\x06sp_pid\x18\x03 \x01(\x04\x12\x13\n\x0bsp_data_evh\x18\x04 \x01(\x04\x12\x16\n\x0esp_control_evh\x18\x05 \x01(\x04\x12\x10\n\x08sp_class\x18\x06 \x01(\x04\x12\x16\n\x0esp_provider_id\x18\x07 \x01(\x04\x12\x11\n\tsp_app_id\x18\x08 \x01(\x04\x12\x17\n\x0fsp_plugin_flags\x18\t \x01(\x04\x12\x1c\n\x14sp_tcp_support_flags\x18\n \x01(\x04\x12\x18\n\x10sp_ev_class_base\x18\x0b \x01(\x04\x12\x16\n\x0esp_plugin_mask\x18\x0c \x01(\x04\x12\x18\n\x10sp_ev_class_name\x18\r \x03(\t\"\xe6\x01\n\x0c\x43puUsageInfo\x12\x11\n\tsvcset_id\x18\x01 \x01(\x04\x12\x19\n\x11svcset_id_present\x18\x02 \x01(\x04\x12\x1b\n\x13\x65xternal_svc_set_id\x18\x03 \x01(\x04\x12\x10\n\x08svc_type\x18\x04 \x01(\x04\x12\x14\n\x0csvc_set_type\x18\x05 \x01(\x04\x12\x14\n\x0csvc_set_name\x18\x06 \x01(\t\x12\x17\n\x0f\x63pu_utilization\x18\x07 \x01(\x04\x12\x10\n\x08\x63pu_zone\x18\x08 \x01(\x04\x12\x10\n\x08\x63pu_load\x18\t \x01(\x02\x12\x10\n\x08\x63pu_user\x18\n \x01(\t\"\x99\x02\n\x0cMemUsageInfo\x12\x11\n\tsvcset_id\x18\x01 \x01(\x04\x12\x19\n\x11svcset_id_present\x18\x02 \x01(\x04\x12\x1b\n\x13\x65xternal_svc_set_id\x18\x03 \x01(\x04\x12\x10\n\x08svc_type\x18\x04 \x01(\x04\x12\x14\n\x0csvc_set_type\x18\x05 \x01(\x04\x12\x14\n\x0csvc_set_name\x18\x06 \x01(\t\x12\x18\n\x10mem_percent_used\x18\x07 \x01(\x02\x12\x16\n\x0emem_bytes_used\x18\x08 \x01(\x04\x12\x10\n\x08mem_zone\x18\t \x01(\x04\x12\x19\n\x11policy_bytes_used\x18\n \x01(\x04\x12!\n\x19policy_bytes_used_percent\x18\x0b \x01(\x04\"\xa7\x02\n\x0cServicesInfo\x12\x11\n\tsvcset_id\x18\x01 \x01(\x04\x12\x19\n\x11svcset_id_present\x18\x02 \x01(\x04\x12\x1b\n\x13\x65xternal_svc_set_id\x18\x03 \x01(\x04\x12\x10\n\x08svc_type\x18\x04 \x01(\x04\x12\x14\n\x0csvc_set_type\x18\x05 \x01(\x04\x12\x14\n\x0csvc_set_name\x18\x06 \x01(\t\x12\x1b\n\x13internal_svc_set_id\x18\x07 \x01(\x04\x12\x1c\n\x14\x61\x63tive_svc_set_count\x18\x08 \x01(\x04\x12\x1b\n\x13total_svc_set_count\x18\t \x01(\x04\x12\x16\n\x0emem_bytes_used\x18\n \x01(\x04\x12\x1e\n\x16mem_bytes_used_percent\x18\x0b \x01(\x04\"\xf3\x02\n\x0bPktDropInfo\x12\x11\n\tsvcset_id\x18\x01 \x01(\x04\x12\x19\n\x11svcset_id_present\x18\x02 \x01(\x04\x12\x1b\n\x13\x65xternal_svc_set_id\x18\x03 \x01(\x04\x12\x10\n\x08svc_type\x18\x04 \x01(\x04\x12\x14\n\x0csvc_set_type\x18\x05 \x01(\x04\x12\x14\n\x0csvc_set_name\x18\x06 \x01(\t\x12\x16\n\x0ememlimit_drops\x18\x07 \x01(\x04\x12\x16\n\x0e\x63pulimit_drops\x18\x08 \x01(\x04\x12\x17\n\x0f\x66lowlimit_drops\x18\t \x01(\x04\x12\x16\n\x0eptclcopy_drops\x18\n \x01(\x04\x12\x1a\n\x12ingress_drop_flows\x18\x0b \x01(\x04\x12\x19\n\x11\x65gress_drop_flows\x18\x0c \x01(\x04\x12!\n\x19\x64rop_exceed_ingress_limit\x18\r \x01(\x04\x12 \n\x18\x64rop_exceed_egress_limit\x18\x0e \x01(\x04:A\n\x10jnprScvsInfraExt\x12\x17.JuniperNetworksSensors\x18N \x01(\x0b\x32\x0e.ServicesInfra')
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


JNPRSCVSINFRAEXT_FIELD_NUMBER = 78
jnprScvsInfraExt = _descriptor.FieldDescriptor(
  name='jnprScvsInfraExt', full_name='jnprScvsInfraExt', index=0,
  number=78, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_SERVICESINFRA = _descriptor.Descriptor(
  name='ServicesInfra',
  full_name='ServicesInfra',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svcs_plugins_info', full_name='ServicesInfra.svcs_plugins_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_cpu_info', full_name='ServicesInfra.svcset_cpu_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_mem_info', full_name='ServicesInfra.svcset_mem_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_svc_info', full_name='ServicesInfra.svcset_svc_info', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_pktdrop_info', full_name='ServicesInfra.svcset_pktdrop_info', index=4,
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
  serialized_start=48,
  serialized_end=267,
)


_PLUGINSINFO = _descriptor.Descriptor(
  name='PluginsInfo',
  full_name='PluginsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sp_num_plugins', full_name='PluginsInfo.sp_num_plugins', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_name', full_name='PluginsInfo.sp_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_pid', full_name='PluginsInfo.sp_pid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_data_evh', full_name='PluginsInfo.sp_data_evh', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_control_evh', full_name='PluginsInfo.sp_control_evh', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_class', full_name='PluginsInfo.sp_class', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_provider_id', full_name='PluginsInfo.sp_provider_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_app_id', full_name='PluginsInfo.sp_app_id', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_plugin_flags', full_name='PluginsInfo.sp_plugin_flags', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_tcp_support_flags', full_name='PluginsInfo.sp_tcp_support_flags', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_ev_class_base', full_name='PluginsInfo.sp_ev_class_base', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_plugin_mask', full_name='PluginsInfo.sp_plugin_mask', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sp_ev_class_name', full_name='PluginsInfo.sp_ev_class_name', index=12,
      number=13, type=9, cpp_type=9, label=3,
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
  serialized_start=270,
  serialized_end=577,
)


_CPUUSAGEINFO = _descriptor.Descriptor(
  name='CpuUsageInfo',
  full_name='CpuUsageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svcset_id', full_name='CpuUsageInfo.svcset_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_id_present', full_name='CpuUsageInfo.svcset_id_present', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_svc_set_id', full_name='CpuUsageInfo.external_svc_set_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_type', full_name='CpuUsageInfo.svc_type', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_type', full_name='CpuUsageInfo.svc_set_type', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_name', full_name='CpuUsageInfo.svc_set_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_utilization', full_name='CpuUsageInfo.cpu_utilization', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_zone', full_name='CpuUsageInfo.cpu_zone', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_load', full_name='CpuUsageInfo.cpu_load', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_user', full_name='CpuUsageInfo.cpu_user', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=580,
  serialized_end=810,
)


_MEMUSAGEINFO = _descriptor.Descriptor(
  name='MemUsageInfo',
  full_name='MemUsageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svcset_id', full_name='MemUsageInfo.svcset_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_id_present', full_name='MemUsageInfo.svcset_id_present', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_svc_set_id', full_name='MemUsageInfo.external_svc_set_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_type', full_name='MemUsageInfo.svc_type', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_type', full_name='MemUsageInfo.svc_set_type', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_name', full_name='MemUsageInfo.svc_set_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_percent_used', full_name='MemUsageInfo.mem_percent_used', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_bytes_used', full_name='MemUsageInfo.mem_bytes_used', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_zone', full_name='MemUsageInfo.mem_zone', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_bytes_used', full_name='MemUsageInfo.policy_bytes_used', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy_bytes_used_percent', full_name='MemUsageInfo.policy_bytes_used_percent', index=10,
      number=11, type=4, cpp_type=4, label=1,
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
  serialized_start=813,
  serialized_end=1094,
)


_SERVICESINFO = _descriptor.Descriptor(
  name='ServicesInfo',
  full_name='ServicesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svcset_id', full_name='ServicesInfo.svcset_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_id_present', full_name='ServicesInfo.svcset_id_present', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_svc_set_id', full_name='ServicesInfo.external_svc_set_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_type', full_name='ServicesInfo.svc_type', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_type', full_name='ServicesInfo.svc_set_type', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_name', full_name='ServicesInfo.svc_set_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='internal_svc_set_id', full_name='ServicesInfo.internal_svc_set_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_svc_set_count', full_name='ServicesInfo.active_svc_set_count', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_svc_set_count', full_name='ServicesInfo.total_svc_set_count', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_bytes_used', full_name='ServicesInfo.mem_bytes_used', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_bytes_used_percent', full_name='ServicesInfo.mem_bytes_used_percent', index=10,
      number=11, type=4, cpp_type=4, label=1,
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
  serialized_start=1097,
  serialized_end=1392,
)


_PKTDROPINFO = _descriptor.Descriptor(
  name='PktDropInfo',
  full_name='PktDropInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svcset_id', full_name='PktDropInfo.svcset_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svcset_id_present', full_name='PktDropInfo.svcset_id_present', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_svc_set_id', full_name='PktDropInfo.external_svc_set_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_type', full_name='PktDropInfo.svc_type', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_type', full_name='PktDropInfo.svc_set_type', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svc_set_name', full_name='PktDropInfo.svc_set_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memlimit_drops', full_name='PktDropInfo.memlimit_drops', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpulimit_drops', full_name='PktDropInfo.cpulimit_drops', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flowlimit_drops', full_name='PktDropInfo.flowlimit_drops', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ptclcopy_drops', full_name='PktDropInfo.ptclcopy_drops', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ingress_drop_flows', full_name='PktDropInfo.ingress_drop_flows', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egress_drop_flows', full_name='PktDropInfo.egress_drop_flows', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop_exceed_ingress_limit', full_name='PktDropInfo.drop_exceed_ingress_limit', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop_exceed_egress_limit', full_name='PktDropInfo.drop_exceed_egress_limit', index=13,
      number=14, type=4, cpp_type=4, label=1,
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
  serialized_start=1395,
  serialized_end=1766,
)

_SERVICESINFRA.fields_by_name['svcs_plugins_info'].message_type = _PLUGINSINFO
_SERVICESINFRA.fields_by_name['svcset_cpu_info'].message_type = _CPUUSAGEINFO
_SERVICESINFRA.fields_by_name['svcset_mem_info'].message_type = _MEMUSAGEINFO
_SERVICESINFRA.fields_by_name['svcset_svc_info'].message_type = _SERVICESINFO
_SERVICESINFRA.fields_by_name['svcset_pktdrop_info'].message_type = _PKTDROPINFO
DESCRIPTOR.message_types_by_name['ServicesInfra'] = _SERVICESINFRA
DESCRIPTOR.message_types_by_name['PluginsInfo'] = _PLUGINSINFO
DESCRIPTOR.message_types_by_name['CpuUsageInfo'] = _CPUUSAGEINFO
DESCRIPTOR.message_types_by_name['MemUsageInfo'] = _MEMUSAGEINFO
DESCRIPTOR.message_types_by_name['ServicesInfo'] = _SERVICESINFO
DESCRIPTOR.message_types_by_name['PktDropInfo'] = _PKTDROPINFO
DESCRIPTOR.extensions_by_name['jnprScvsInfraExt'] = jnprScvsInfraExt

ServicesInfra = _reflection.GeneratedProtocolMessageType('ServicesInfra', (_message.Message,), dict(
  DESCRIPTOR = _SERVICESINFRA,
  __module__ = 'svcset_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:ServicesInfra)
  ))
_sym_db.RegisterMessage(ServicesInfra)

PluginsInfo = _reflection.GeneratedProtocolMessageType('PluginsInfo', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINSINFO,
  __module__ = 'svcset_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:PluginsInfo)
  ))
_sym_db.RegisterMessage(PluginsInfo)

CpuUsageInfo = _reflection.GeneratedProtocolMessageType('CpuUsageInfo', (_message.Message,), dict(
  DESCRIPTOR = _CPUUSAGEINFO,
  __module__ = 'svcset_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:CpuUsageInfo)
  ))
_sym_db.RegisterMessage(CpuUsageInfo)

MemUsageInfo = _reflection.GeneratedProtocolMessageType('MemUsageInfo', (_message.Message,), dict(
  DESCRIPTOR = _MEMUSAGEINFO,
  __module__ = 'svcset_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:MemUsageInfo)
  ))
_sym_db.RegisterMessage(MemUsageInfo)

ServicesInfo = _reflection.GeneratedProtocolMessageType('ServicesInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVICESINFO,
  __module__ = 'svcset_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:ServicesInfo)
  ))
_sym_db.RegisterMessage(ServicesInfo)

PktDropInfo = _reflection.GeneratedProtocolMessageType('PktDropInfo', (_message.Message,), dict(
  DESCRIPTOR = _PKTDROPINFO,
  __module__ = 'svcset_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:PktDropInfo)
  ))
_sym_db.RegisterMessage(PktDropInfo)

jnprScvsInfraExt.message_type = _SERVICESINFRA
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(jnprScvsInfraExt)

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
