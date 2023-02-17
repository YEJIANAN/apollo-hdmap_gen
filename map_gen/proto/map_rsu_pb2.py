# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_rsu.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import map_id_pb2 as map__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_rsu.proto',
  package='hdmap',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmap_rsu.proto\x12\x05hdmap\x1a\x0cmap_id.proto\"[\n\x03RSU\x12\x15\n\x02id\x18\x01 \x01(\x0b\x32\t.hdmap.Id\x12\x1e\n\x0bjunction_id\x18\x02 \x01(\x0b\x32\t.hdmap.Id\x12\x1d\n\noverlap_id\x18\x03 \x03(\x0b\x32\t.hdmap.Id'
  ,
  dependencies=[map__id__pb2.DESCRIPTOR,])




_RSU = _descriptor.Descriptor(
  name='RSU',
  full_name='hdmap.RSU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hdmap.RSU.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='junction_id', full_name='hdmap.RSU.junction_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overlap_id', full_name='hdmap.RSU.overlap_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=129,
)

_RSU.fields_by_name['id'].message_type = map__id__pb2._ID
_RSU.fields_by_name['junction_id'].message_type = map__id__pb2._ID
_RSU.fields_by_name['overlap_id'].message_type = map__id__pb2._ID
DESCRIPTOR.message_types_by_name['RSU'] = _RSU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RSU = _reflection.GeneratedProtocolMessageType('RSU', (_message.Message,), {
  'DESCRIPTOR' : _RSU,
  '__module__' : 'map_rsu_pb2'
  # @@protoc_insertion_point(class_scope:hdmap.RSU)
  })
_sym_db.RegisterMessage(RSU)


# @@protoc_insertion_point(module_scope)
