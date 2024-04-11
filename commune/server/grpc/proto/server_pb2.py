# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cserver.proto\"G\n\tDataBlock\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x10\n\x08metadata\x18\x02 \x01(\x0c\x12\x1a\n\x06\x62locks\x18\x03 \x03(\x0b\x32\n.DataBlock2-\n\x06Server\x12#\n\x07\x46orward\x12\n.DataBlock\x1a\n.DataBlock\"\x00\x62\x06proto3'
)




_DATABLOCK = _descriptor.Descriptor(
  name='DataBlock',
  full_name='DataBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataBlock.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='DataBlock.metadata', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='DataBlock.blocks', index=2,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=87,
)

_DATABLOCK.fields_by_name['blocks'].message_type = _DATABLOCK
DESCRIPTOR.message_types_by_name['DataBlock'] = _DATABLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataBlock = _reflection.GeneratedProtocolMessageType('DataBlock', (_message.Message,), {
  'DESCRIPTOR' : _DATABLOCK,
  '__module__' : 'server_pb2'
  # @@protoc_insertion_point(class_scope:DataBlock)
  })
_sym_db.RegisterMessage(DataBlock)



_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='Server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=89,
  serialized_end=134,
  methods=[
  _descriptor.MethodDescriptor(
    name='Forward',
    full_name='Server.Forward',
    index=0,
    containing_service=None,
    input_type=_DATABLOCK,
    output_type=_DATABLOCK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)
