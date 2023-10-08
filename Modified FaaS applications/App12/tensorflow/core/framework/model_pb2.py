# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/model.proto',
  package='tensorflow.data.model',
  syntax='proto3',
  serialized_options=_b('ZLgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/model_go_proto\370\001\001'),
  serialized_pb=_b('\n%tensorflow/core/framework/model.proto\x12\x15tensorflow.data.model\"\xcb\x07\n\nModelProto\x12\x36\n\x06output\x18\x01 \x01(\x0b\x32&.tensorflow.data.model.ModelProto.Node\x12\x12\n\nid_counter\x18\x02 \x01(\x03\x12\x1e\n\x16\x63ollect_resource_usage\x18\x03 \x01(\x08\x12Q\n\x13optimization_params\x18\x04 \x01(\x0b\x32\x34.tensorflow.data.model.ModelProto.OptimizationParams\x1a\xe7\x04\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x61utotune\x18\x03 \x01(\x08\x12\x16\n\x0e\x62uffered_bytes\x18\x04 \x01(\x03\x12\x19\n\x11\x62uffered_elements\x18\x05 \x01(\x03\x12\x16\n\x0e\x62ytes_consumed\x18\x06 \x01(\x03\x12\x16\n\x0e\x62ytes_produced\x18\x07 \x01(\x03\x12\x14\n\x0cnum_elements\x18\x08 \x01(\x03\x12\x17\n\x0fprocessing_time\x18\t \x01(\x03\x12\x16\n\x0erecord_metrics\x18\n \x01(\x08\x12\x44\n\nparameters\x18\x0b \x03(\x0b\x32\x30.tensorflow.data.model.ModelProto.Node.Parameter\x12!\n\x19input_processing_time_sum\x18\x0c \x01(\x01\x12#\n\x1binput_processing_time_count\x18\r \x01(\x03\x12\x36\n\x06inputs\x18\x0e \x03(\x0b\x32&.tensorflow.data.model.ModelProto.Node\x12\x34\n\nnode_class\x18\x0f \x01(\x0e\x32 .tensorflow.data.model.NodeClass\x12\r\n\x05ratio\x18\x10 \x01(\x01\x12\x14\n\x0cmemory_ratio\x18\x11 \x01(\x01\x1ah\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x13\n\x0bstate_value\x18\x03 \x01(\x01\x12\x0b\n\x03min\x18\x04 \x01(\x01\x12\x0b\n\x03max\x18\x05 \x01(\x01\x12\x0f\n\x07tunable\x18\x06 \x01(\x08\x1a\x93\x01\n\x12OptimizationParams\x12;\n\talgorithm\x18\x01 \x01(\x0e\x32(.tensorflow.data.model.AutotuneAlgorithm\x12\x12\n\ncpu_budget\x18\x02 \x01(\x03\x12\x12\n\nram_budget\x18\x03 \x01(\x03\x12\x18\n\x10model_input_time\x18\x04 \x01(\x01*\x83\x01\n\tNodeClass\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fINTERLEAVE_MANY\x10\x01\x12\x19\n\x15\x41SYNC_INTERLEAVE_MANY\x10\x02\x12\x0f\n\x0bKNOWN_RATIO\x10\x03\x12\x15\n\x11\x41SYNC_KNOWN_RATIO\x10\x04\x12\x11\n\rUNKNOWN_RATIO\x10\x05*9\n\x11\x41utotuneAlgorithm\x12\x0e\n\nHILL_CLIMB\x10\x00\x12\x14\n\x10GRADIENT_DESCENT\x10\x01\x42QZLgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/model_go_proto\xf8\x01\x01\x62\x06proto3')
)

_NODECLASS = _descriptor.EnumDescriptor(
  name='NodeClass',
  full_name='tensorflow.data.model.NodeClass',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERLEAVE_MANY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASYNC_INTERLEAVE_MANY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KNOWN_RATIO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASYNC_KNOWN_RATIO', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_RATIO', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1039,
  serialized_end=1170,
)
_sym_db.RegisterEnumDescriptor(_NODECLASS)

NodeClass = enum_type_wrapper.EnumTypeWrapper(_NODECLASS)
_AUTOTUNEALGORITHM = _descriptor.EnumDescriptor(
  name='AutotuneAlgorithm',
  full_name='tensorflow.data.model.AutotuneAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HILL_CLIMB', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRADIENT_DESCENT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1172,
  serialized_end=1229,
)
_sym_db.RegisterEnumDescriptor(_AUTOTUNEALGORITHM)

AutotuneAlgorithm = enum_type_wrapper.EnumTypeWrapper(_AUTOTUNEALGORITHM)
UNKNOWN = 0
INTERLEAVE_MANY = 1
ASYNC_INTERLEAVE_MANY = 2
KNOWN_RATIO = 3
ASYNC_KNOWN_RATIO = 4
UNKNOWN_RATIO = 5
HILL_CLIMB = 0
GRADIENT_DESCENT = 1



_MODELPROTO_NODE_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='tensorflow.data.model.ModelProto.Node.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.data.model.ModelProto.Node.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.data.model.ModelProto.Node.Parameter.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_value', full_name='tensorflow.data.model.ModelProto.Node.Parameter.state_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='tensorflow.data.model.ModelProto.Node.Parameter.min', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='tensorflow.data.model.ModelProto.Node.Parameter.max', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tunable', full_name='tensorflow.data.model.ModelProto.Node.Parameter.tunable', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=782,
  serialized_end=886,
)

_MODELPROTO_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='tensorflow.data.model.ModelProto.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.data.model.ModelProto.Node.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.data.model.ModelProto.Node.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autotune', full_name='tensorflow.data.model.ModelProto.Node.autotune', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffered_bytes', full_name='tensorflow.data.model.ModelProto.Node.buffered_bytes', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffered_elements', full_name='tensorflow.data.model.ModelProto.Node.buffered_elements', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_consumed', full_name='tensorflow.data.model.ModelProto.Node.bytes_consumed', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_produced', full_name='tensorflow.data.model.ModelProto.Node.bytes_produced', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_elements', full_name='tensorflow.data.model.ModelProto.Node.num_elements', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processing_time', full_name='tensorflow.data.model.ModelProto.Node.processing_time', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record_metrics', full_name='tensorflow.data.model.ModelProto.Node.record_metrics', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='tensorflow.data.model.ModelProto.Node.parameters', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_processing_time_sum', full_name='tensorflow.data.model.ModelProto.Node.input_processing_time_sum', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_processing_time_count', full_name='tensorflow.data.model.ModelProto.Node.input_processing_time_count', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tensorflow.data.model.ModelProto.Node.inputs', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_class', full_name='tensorflow.data.model.ModelProto.Node.node_class', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratio', full_name='tensorflow.data.model.ModelProto.Node.ratio', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_ratio', full_name='tensorflow.data.model.ModelProto.Node.memory_ratio', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MODELPROTO_NODE_PARAMETER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=886,
)

_MODELPROTO_OPTIMIZATIONPARAMS = _descriptor.Descriptor(
  name='OptimizationParams',
  full_name='tensorflow.data.model.ModelProto.OptimizationParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='tensorflow.data.model.ModelProto.OptimizationParams.algorithm', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_budget', full_name='tensorflow.data.model.ModelProto.OptimizationParams.cpu_budget', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ram_budget', full_name='tensorflow.data.model.ModelProto.OptimizationParams.ram_budget', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_input_time', full_name='tensorflow.data.model.ModelProto.OptimizationParams.model_input_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=889,
  serialized_end=1036,
)

_MODELPROTO = _descriptor.Descriptor(
  name='ModelProto',
  full_name='tensorflow.data.model.ModelProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='tensorflow.data.model.ModelProto.output', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_counter', full_name='tensorflow.data.model.ModelProto.id_counter', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collect_resource_usage', full_name='tensorflow.data.model.ModelProto.collect_resource_usage', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimization_params', full_name='tensorflow.data.model.ModelProto.optimization_params', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MODELPROTO_NODE, _MODELPROTO_OPTIMIZATIONPARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=1036,
)

_MODELPROTO_NODE_PARAMETER.containing_type = _MODELPROTO_NODE
_MODELPROTO_NODE.fields_by_name['parameters'].message_type = _MODELPROTO_NODE_PARAMETER
_MODELPROTO_NODE.fields_by_name['inputs'].message_type = _MODELPROTO_NODE
_MODELPROTO_NODE.fields_by_name['node_class'].enum_type = _NODECLASS
_MODELPROTO_NODE.containing_type = _MODELPROTO
_MODELPROTO_OPTIMIZATIONPARAMS.fields_by_name['algorithm'].enum_type = _AUTOTUNEALGORITHM
_MODELPROTO_OPTIMIZATIONPARAMS.containing_type = _MODELPROTO
_MODELPROTO.fields_by_name['output'].message_type = _MODELPROTO_NODE
_MODELPROTO.fields_by_name['optimization_params'].message_type = _MODELPROTO_OPTIMIZATIONPARAMS
DESCRIPTOR.message_types_by_name['ModelProto'] = _MODELPROTO
DESCRIPTOR.enum_types_by_name['NodeClass'] = _NODECLASS
DESCRIPTOR.enum_types_by_name['AutotuneAlgorithm'] = _AUTOTUNEALGORITHM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelProto = _reflection.GeneratedProtocolMessageType('ModelProto', (_message.Message,), {

  'Node' : _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {

    'Parameter' : _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
      'DESCRIPTOR' : _MODELPROTO_NODE_PARAMETER,
      '__module__' : 'tensorflow.core.framework.model_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.data.model.ModelProto.Node.Parameter)
      })
    ,
    'DESCRIPTOR' : _MODELPROTO_NODE,
    '__module__' : 'tensorflow.core.framework.model_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.data.model.ModelProto.Node)
    })
  ,

  'OptimizationParams' : _reflection.GeneratedProtocolMessageType('OptimizationParams', (_message.Message,), {
    'DESCRIPTOR' : _MODELPROTO_OPTIMIZATIONPARAMS,
    '__module__' : 'tensorflow.core.framework.model_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.data.model.ModelProto.OptimizationParams)
    })
  ,
  'DESCRIPTOR' : _MODELPROTO,
  '__module__' : 'tensorflow.core.framework.model_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.model.ModelProto)
  })
_sym_db.RegisterMessage(ModelProto)
_sym_db.RegisterMessage(ModelProto.Node)
_sym_db.RegisterMessage(ModelProto.Node.Parameter)
_sym_db.RegisterMessage(ModelProto.OptimizationParams)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
