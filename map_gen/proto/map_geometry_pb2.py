# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_geometry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_geometry.proto',
  package='hdmap',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12map_geometry.proto\x12\x05hdmap\x1a\x0egeometry.proto\"*\n\x07Polygon\x12\x1f\n\x05point\x18\x01 \x03(\x0b\x32\x10.common.PointENU\".\n\x0bLineSegment\x12\x1f\n\x05point\x18\x01 \x03(\x0b\x32\x10.common.PointENU\"\x9e\x01\n\x0c\x43urveSegment\x12*\n\x0cline_segment\x18\x01 \x01(\x0b\x32\x12.hdmap.LineSegmentH\x00\x12\t\n\x01s\x18\x06 \x01(\x01\x12(\n\x0estart_position\x18\x07 \x01(\x0b\x32\x10.common.PointENU\x12\x0f\n\x07heading\x18\x08 \x01(\x01\x12\x0e\n\x06length\x18\t \x01(\x01\x42\x0c\n\ncurve_type\"-\n\x05\x43urve\x12$\n\x07segment\x18\x01 \x03(\x0b\x32\x13.hdmap.CurveSegment'
  ,
  dependencies=[geometry__pb2.DESCRIPTOR,])




_POLYGON = _descriptor.Descriptor(
  name='Polygon',
  full_name='hdmap.Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='hdmap.Polygon.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=45,
  serialized_end=87,
)


_LINESEGMENT = _descriptor.Descriptor(
  name='LineSegment',
  full_name='hdmap.LineSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='hdmap.LineSegment.point', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=89,
  serialized_end=135,
)


_CURVESEGMENT = _descriptor.Descriptor(
  name='CurveSegment',
  full_name='hdmap.CurveSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='line_segment', full_name='hdmap.CurveSegment.line_segment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s', full_name='hdmap.CurveSegment.s', index=1,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_position', full_name='hdmap.CurveSegment.start_position', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='hdmap.CurveSegment.heading', index=3,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='hdmap.CurveSegment.length', index=4,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
    _descriptor.OneofDescriptor(
      name='curve_type', full_name='hdmap.CurveSegment.curve_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=138,
  serialized_end=296,
)


_CURVE = _descriptor.Descriptor(
  name='Curve',
  full_name='hdmap.Curve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='hdmap.Curve.segment', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=298,
  serialized_end=343,
)

_POLYGON.fields_by_name['point'].message_type = geometry__pb2._POINTENU
_LINESEGMENT.fields_by_name['point'].message_type = geometry__pb2._POINTENU
_CURVESEGMENT.fields_by_name['line_segment'].message_type = _LINESEGMENT
_CURVESEGMENT.fields_by_name['start_position'].message_type = geometry__pb2._POINTENU
_CURVESEGMENT.oneofs_by_name['curve_type'].fields.append(
  _CURVESEGMENT.fields_by_name['line_segment'])
_CURVESEGMENT.fields_by_name['line_segment'].containing_oneof = _CURVESEGMENT.oneofs_by_name['curve_type']
_CURVE.fields_by_name['segment'].message_type = _CURVESEGMENT
DESCRIPTOR.message_types_by_name['Polygon'] = _POLYGON
DESCRIPTOR.message_types_by_name['LineSegment'] = _LINESEGMENT
DESCRIPTOR.message_types_by_name['CurveSegment'] = _CURVESEGMENT
DESCRIPTOR.message_types_by_name['Curve'] = _CURVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:hdmap.Polygon)
  })
_sym_db.RegisterMessage(Polygon)

LineSegment = _reflection.GeneratedProtocolMessageType('LineSegment', (_message.Message,), {
  'DESCRIPTOR' : _LINESEGMENT,
  '__module__' : 'map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:hdmap.LineSegment)
  })
_sym_db.RegisterMessage(LineSegment)

CurveSegment = _reflection.GeneratedProtocolMessageType('CurveSegment', (_message.Message,), {
  'DESCRIPTOR' : _CURVESEGMENT,
  '__module__' : 'map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:hdmap.CurveSegment)
  })
_sym_db.RegisterMessage(CurveSegment)

Curve = _reflection.GeneratedProtocolMessageType('Curve', (_message.Message,), {
  'DESCRIPTOR' : _CURVE,
  '__module__' : 'map_geometry_pb2'
  # @@protoc_insertion_point(class_scope:hdmap.Curve)
  })
_sym_db.RegisterMessage(Curve)


# @@protoc_insertion_point(module_scope)
