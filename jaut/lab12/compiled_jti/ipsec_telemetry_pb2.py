# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ipsec_telemetry.proto

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
  name='ipsec_telemetry.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15ipsec_telemetry.proto\x1a\x13telemetry_top.proto\"\x97\x01\n\x08IPsecVPN\x12+\n\x11ipsec_global_info\x18\x01 \x03(\x0b\x32\x10.IPsecGlobalInfo\x12.\n\x11ipsec_svcset_info\x18\x02 \x03(\x0b\x32\x13.IPsecPerSvcsetInfo\x12.\n\x11ipsec_tunnel_info\x18\x03 \x03(\x0b\x32\x13.IPsecPerTunnelInfo\"\xde\x02\n\x0fIPsecGlobalInfo\x12\x18\n\x10re_pconn_connect\x18\x01 \x01(\x04\x12\x14\n\x0cpconn_status\x18\x02 \x01(\x04\x12\x1e\n\x16sa_trigger_enq_success\x18\x03 \x01(\x04\x12\x1b\n\x13sa_trigger_enq_fail\x18\x04 \x01(\x04\x12 \n\x18sa_trigger_retry_success\x18\x05 \x01(\x04\x12\x1d\n\x15sa_trigger_retry_fail\x18\x06 \x01(\x04\x12\x17\n\x0fsa_trigger_sent\x18\x07 \x01(\x04\x12\x17\n\x0fsa_trigger_fail\x18\x08 \x01(\x04\x12\x18\n\x10sa_trigger_alloc\x18\t \x01(\x04\x12\x1d\n\x15sa_trigger_alloc_fail\x18\n \x01(\x04\x12\x17\n\x0fsa_trigger_free\x18\x0b \x01(\x04\x12\x19\n\x11sa_trig_enq_count\x18\x0c \x01(\x04\"\xdf\x01\n\x12IPsecPerSvcsetInfo\x12\x11\n\tsvcset_id\x18\x01 \x02(\x04\x12\x1a\n\x12rule_lookup_failed\x18\x02 \x01(\x04\x12\x18\n\x10sa_lookup_failed\x18\x03 \x01(\x04\x12\x1a\n\x12\x65xceeds_tunnel_mtu\x18\x04 \x01(\x04\x12\x1a\n\x12\x63lear_pkt_received\x18\x05 \x01(\x04\x12\x18\n\x10\x65sp_pkt_received\x18\x06 \x01(\x04\x12\x16\n\x0e\x65ncap_callback\x18\x07 \x01(\x04\x12\x16\n\x0e\x64\x65\x63\x61p_callback\x18\x08 \x01(\x04\"\xaf\x04\n\x12IPsecPerTunnelInfo\x12\x11\n\ttunnel_id\x18\x01 \x02(\x04\x12\x13\n\x0b\x65sp_rplzero\x18\x02 \x01(\x04\x12\x19\n\x11ipsec_bad_headers\x18\x03 \x01(\x04\x12\x18\n\x10\x65sp_bad_trailers\x18\x04 \x01(\x04\x12\x1b\n\x13\x64\x65\x63\x61p_nxt_proto_err\x18\x05 \x01(\x04\x12\x1b\n\x13\x64\x65\x63\x61p_inner_len_err\x18\x06 \x01(\x04\x12\x15\n\rdecap_hdr_err\x18\x07 \x01(\x04\x12\x1d\n\x15\x64\x65\x63\x61p_inner_saddr_err\x18\x08 \x01(\x04\x12\x1d\n\x15\x64\x65\x63\x61p_inner_daddr_err\x18\t \x01(\x04\x12\x1b\n\x13\x64\x65\x63\x61p_sn_alloc_fail\x18\n \x01(\x04\x12\x19\n\x11\x64\x65\x63\x61p_sn_ext_fail\x18\x0b \x01(\x04\x12\x17\n\x0f\x65sp_auth_failed\x18\x0c \x01(\x04\x12\x1b\n\x13\x64\x65\x63\x61p_reinject_fail\x18\r \x01(\x04\x12\x1f\n\x17\x64\x65\x63\x61p_sn_transient_drop\x18\x0e \x01(\x04\x12\x1b\n\x13\x65sp_rplbeforewindow\x18\x0f \x01(\x04\x12\x18\n\x10\x65sp_rplduplicate\x18\x10 \x01(\x04\x12 \n\x18\x65sp_protected_bytes_sent\x18\x11 \x01(\x04\x12!\n\x19\x65sp_protected_bytes_recvd\x18\x12 \x01(\x04\x12\x10\n\x08\x65ncrypts\x18\x13 \x01(\x04\x12\x10\n\x08\x64\x65\x63rypts\x18\x14 \x01(\x04:;\n\x0fjnprIPsecVPNExt\x12\x17.JuniperNetworksSensors\x18M \x01(\x0b\x32\t.IPsecVPN')
  ,
  dependencies=[telemetry__top__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


JNPRIPSECVPNEXT_FIELD_NUMBER = 77
jnprIPsecVPNExt = _descriptor.FieldDescriptor(
  name='jnprIPsecVPNExt', full_name='jnprIPsecVPNExt', index=0,
  number=77, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_IPSECVPN = _descriptor.Descriptor(
  name='IPsecVPN',
  full_name='IPsecVPN',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipsec_global_info', full_name='IPsecVPN.ipsec_global_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipsec_svcset_info', full_name='IPsecVPN.ipsec_svcset_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipsec_tunnel_info', full_name='IPsecVPN.ipsec_tunnel_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=47,
  serialized_end=198,
)


_IPSECGLOBALINFO = _descriptor.Descriptor(
  name='IPsecGlobalInfo',
  full_name='IPsecGlobalInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='re_pconn_connect', full_name='IPsecGlobalInfo.re_pconn_connect', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pconn_status', full_name='IPsecGlobalInfo.pconn_status', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_enq_success', full_name='IPsecGlobalInfo.sa_trigger_enq_success', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_enq_fail', full_name='IPsecGlobalInfo.sa_trigger_enq_fail', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_retry_success', full_name='IPsecGlobalInfo.sa_trigger_retry_success', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_retry_fail', full_name='IPsecGlobalInfo.sa_trigger_retry_fail', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_sent', full_name='IPsecGlobalInfo.sa_trigger_sent', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_fail', full_name='IPsecGlobalInfo.sa_trigger_fail', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_alloc', full_name='IPsecGlobalInfo.sa_trigger_alloc', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_alloc_fail', full_name='IPsecGlobalInfo.sa_trigger_alloc_fail', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trigger_free', full_name='IPsecGlobalInfo.sa_trigger_free', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_trig_enq_count', full_name='IPsecGlobalInfo.sa_trig_enq_count', index=11,
      number=12, type=4, cpp_type=4, label=1,
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
  serialized_start=201,
  serialized_end=551,
)


_IPSECPERSVCSETINFO = _descriptor.Descriptor(
  name='IPsecPerSvcsetInfo',
  full_name='IPsecPerSvcsetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svcset_id', full_name='IPsecPerSvcsetInfo.svcset_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rule_lookup_failed', full_name='IPsecPerSvcsetInfo.rule_lookup_failed', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sa_lookup_failed', full_name='IPsecPerSvcsetInfo.sa_lookup_failed', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exceeds_tunnel_mtu', full_name='IPsecPerSvcsetInfo.exceeds_tunnel_mtu', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clear_pkt_received', full_name='IPsecPerSvcsetInfo.clear_pkt_received', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_pkt_received', full_name='IPsecPerSvcsetInfo.esp_pkt_received', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encap_callback', full_name='IPsecPerSvcsetInfo.encap_callback', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_callback', full_name='IPsecPerSvcsetInfo.decap_callback', index=7,
      number=8, type=4, cpp_type=4, label=1,
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
  serialized_start=554,
  serialized_end=777,
)


_IPSECPERTUNNELINFO = _descriptor.Descriptor(
  name='IPsecPerTunnelInfo',
  full_name='IPsecPerTunnelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tunnel_id', full_name='IPsecPerTunnelInfo.tunnel_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_rplzero', full_name='IPsecPerTunnelInfo.esp_rplzero', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ipsec_bad_headers', full_name='IPsecPerTunnelInfo.ipsec_bad_headers', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_bad_trailers', full_name='IPsecPerTunnelInfo.esp_bad_trailers', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_nxt_proto_err', full_name='IPsecPerTunnelInfo.decap_nxt_proto_err', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_inner_len_err', full_name='IPsecPerTunnelInfo.decap_inner_len_err', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_hdr_err', full_name='IPsecPerTunnelInfo.decap_hdr_err', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_inner_saddr_err', full_name='IPsecPerTunnelInfo.decap_inner_saddr_err', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_inner_daddr_err', full_name='IPsecPerTunnelInfo.decap_inner_daddr_err', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_sn_alloc_fail', full_name='IPsecPerTunnelInfo.decap_sn_alloc_fail', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_sn_ext_fail', full_name='IPsecPerTunnelInfo.decap_sn_ext_fail', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_auth_failed', full_name='IPsecPerTunnelInfo.esp_auth_failed', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_reinject_fail', full_name='IPsecPerTunnelInfo.decap_reinject_fail', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decap_sn_transient_drop', full_name='IPsecPerTunnelInfo.decap_sn_transient_drop', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_rplbeforewindow', full_name='IPsecPerTunnelInfo.esp_rplbeforewindow', index=14,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_rplduplicate', full_name='IPsecPerTunnelInfo.esp_rplduplicate', index=15,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_protected_bytes_sent', full_name='IPsecPerTunnelInfo.esp_protected_bytes_sent', index=16,
      number=17, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esp_protected_bytes_recvd', full_name='IPsecPerTunnelInfo.esp_protected_bytes_recvd', index=17,
      number=18, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypts', full_name='IPsecPerTunnelInfo.encrypts', index=18,
      number=19, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decrypts', full_name='IPsecPerTunnelInfo.decrypts', index=19,
      number=20, type=4, cpp_type=4, label=1,
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
  serialized_start=780,
  serialized_end=1339,
)

_IPSECVPN.fields_by_name['ipsec_global_info'].message_type = _IPSECGLOBALINFO
_IPSECVPN.fields_by_name['ipsec_svcset_info'].message_type = _IPSECPERSVCSETINFO
_IPSECVPN.fields_by_name['ipsec_tunnel_info'].message_type = _IPSECPERTUNNELINFO
DESCRIPTOR.message_types_by_name['IPsecVPN'] = _IPSECVPN
DESCRIPTOR.message_types_by_name['IPsecGlobalInfo'] = _IPSECGLOBALINFO
DESCRIPTOR.message_types_by_name['IPsecPerSvcsetInfo'] = _IPSECPERSVCSETINFO
DESCRIPTOR.message_types_by_name['IPsecPerTunnelInfo'] = _IPSECPERTUNNELINFO
DESCRIPTOR.extensions_by_name['jnprIPsecVPNExt'] = jnprIPsecVPNExt

IPsecVPN = _reflection.GeneratedProtocolMessageType('IPsecVPN', (_message.Message,), dict(
  DESCRIPTOR = _IPSECVPN,
  __module__ = 'ipsec_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:IPsecVPN)
  ))
_sym_db.RegisterMessage(IPsecVPN)

IPsecGlobalInfo = _reflection.GeneratedProtocolMessageType('IPsecGlobalInfo', (_message.Message,), dict(
  DESCRIPTOR = _IPSECGLOBALINFO,
  __module__ = 'ipsec_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:IPsecGlobalInfo)
  ))
_sym_db.RegisterMessage(IPsecGlobalInfo)

IPsecPerSvcsetInfo = _reflection.GeneratedProtocolMessageType('IPsecPerSvcsetInfo', (_message.Message,), dict(
  DESCRIPTOR = _IPSECPERSVCSETINFO,
  __module__ = 'ipsec_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:IPsecPerSvcsetInfo)
  ))
_sym_db.RegisterMessage(IPsecPerSvcsetInfo)

IPsecPerTunnelInfo = _reflection.GeneratedProtocolMessageType('IPsecPerTunnelInfo', (_message.Message,), dict(
  DESCRIPTOR = _IPSECPERTUNNELINFO,
  __module__ = 'ipsec_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:IPsecPerTunnelInfo)
  ))
_sym_db.RegisterMessage(IPsecPerTunnelInfo)

jnprIPsecVPNExt.message_type = _IPSECVPN
telemetry__top__pb2.JuniperNetworksSensors.RegisterExtension(jnprIPsecVPNExt)

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
