# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/rna_quantification.proto

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


from ga4gh import metadata_pb2 as ga4gh_dot_metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/rna_quantification.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\x1ega4gh/rna_quantification.proto\x12\x05ga4gh\x1a\x14ga4gh/metadata.proto\"D\n\x14RnaQuantificationSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xb8\x01\n\x11RnaQuantification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x16\n\x0eread_group_ids\x18\x04 \x03(\t\x12 \n\x08programs\x18\x05 \x03(\x0b\x32\x0e.ga4gh.Program\x12\x17\n\x0f\x66\x65\x61ture_set_ids\x18\x06 \x03(\t\x12!\n\x19rna_quantification_set_id\x18\x07 \x01(\t\"\x8d\x02\n\x0f\x45xpressionLevel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nfeature_id\x18\x03 \x01(\t\x12\x1d\n\x15rna_quantification_id\x18\x04 \x01(\t\x12\x16\n\x0eraw_read_count\x18\x05 \x01(\x02\x12\x12\n\nexpression\x18\x06 \x01(\x02\x12\x15\n\ris_normalized\x18\x07 \x01(\x08\x12$\n\x05units\x18\x08 \x01(\x0e\x32\x15.ga4gh.ExpressionUnit\x12\r\n\x05score\x18\t \x01(\x02\x12\x19\n\x11\x63onf_interval_low\x18\n \x01(\x02\x12\x1a\n\x12\x63onf_interval_high\x18\x0b \x01(\x02*D\n\x0e\x45xpressionUnit\x12\x1f\n\x1b\x45XPRESSION_UNIT_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46PKM\x10\x01\x12\x07\n\x03TPM\x10\x02\x62\x06proto3')
  ,
  dependencies=[ga4gh_dot_metadata__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EXPRESSIONUNIT = _descriptor.EnumDescriptor(
  name='ExpressionUnit',
  full_name='ga4gh.ExpressionUnit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPRESSION_UNIT_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FPKM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPM', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=592,
  serialized_end=660,
)
_sym_db.RegisterEnumDescriptor(_EXPRESSIONUNIT)

ExpressionUnit = enum_type_wrapper.EnumTypeWrapper(_EXPRESSIONUNIT)
EXPRESSION_UNIT_UNSPECIFIED = 0
FPKM = 1
TPM = 2



_RNAQUANTIFICATIONSET = _descriptor.Descriptor(
  name='RnaQuantificationSet',
  full_name='ga4gh.RnaQuantificationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.RnaQuantificationSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.RnaQuantificationSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.RnaQuantificationSet.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=131,
)


_RNAQUANTIFICATION = _descriptor.Descriptor(
  name='RnaQuantification',
  full_name='ga4gh.RnaQuantification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.RnaQuantification.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.RnaQuantification.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.RnaQuantification.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_group_ids', full_name='ga4gh.RnaQuantification.read_group_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='programs', full_name='ga4gh.RnaQuantification.programs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_set_ids', full_name='ga4gh.RnaQuantification.feature_set_ids', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rna_quantification_set_id', full_name='ga4gh.RnaQuantification.rna_quantification_set_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=318,
)


_EXPRESSIONLEVEL = _descriptor.Descriptor(
  name='ExpressionLevel',
  full_name='ga4gh.ExpressionLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.ExpressionLevel.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.ExpressionLevel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_id', full_name='ga4gh.ExpressionLevel.feature_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rna_quantification_id', full_name='ga4gh.ExpressionLevel.rna_quantification_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_read_count', full_name='ga4gh.ExpressionLevel.raw_read_count', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expression', full_name='ga4gh.ExpressionLevel.expression', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_normalized', full_name='ga4gh.ExpressionLevel.is_normalized', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='ga4gh.ExpressionLevel.units', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='ga4gh.ExpressionLevel.score', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conf_interval_low', full_name='ga4gh.ExpressionLevel.conf_interval_low', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conf_interval_high', full_name='ga4gh.ExpressionLevel.conf_interval_high', index=10,
      number=11, type=2, cpp_type=6, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=590,
)

_RNAQUANTIFICATION.fields_by_name['programs'].message_type = ga4gh_dot_metadata__pb2._PROGRAM
_EXPRESSIONLEVEL.fields_by_name['units'].enum_type = _EXPRESSIONUNIT
DESCRIPTOR.message_types_by_name['RnaQuantificationSet'] = _RNAQUANTIFICATIONSET
DESCRIPTOR.message_types_by_name['RnaQuantification'] = _RNAQUANTIFICATION
DESCRIPTOR.message_types_by_name['ExpressionLevel'] = _EXPRESSIONLEVEL
DESCRIPTOR.enum_types_by_name['ExpressionUnit'] = _EXPRESSIONUNIT

RnaQuantificationSet = _reflection.GeneratedProtocolMessageType('RnaQuantificationSet', (_message.Message,), dict(
  DESCRIPTOR = _RNAQUANTIFICATIONSET,
  __module__ = 'ga4gh.rna_quantification_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.RnaQuantificationSet)
  ))
_sym_db.RegisterMessage(RnaQuantificationSet)

RnaQuantification = _reflection.GeneratedProtocolMessageType('RnaQuantification', (_message.Message,), dict(
  DESCRIPTOR = _RNAQUANTIFICATION,
  __module__ = 'ga4gh.rna_quantification_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.RnaQuantification)
  ))
_sym_db.RegisterMessage(RnaQuantification)

ExpressionLevel = _reflection.GeneratedProtocolMessageType('ExpressionLevel', (_message.Message,), dict(
  DESCRIPTOR = _EXPRESSIONLEVEL,
  __module__ = 'ga4gh.rna_quantification_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.ExpressionLevel)
  ))
_sym_db.RegisterMessage(ExpressionLevel)


# @@protoc_insertion_point(module_scope)
