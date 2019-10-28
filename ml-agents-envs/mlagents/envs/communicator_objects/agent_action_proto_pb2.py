# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents/envs/communicator_objects/agent_action_proto.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mlagents.envs.communicator_objects import (
    custom_action_pb2 as mlagents_dot_envs_dot_communicator__objects_dot_custom__action__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="mlagents/envs/communicator_objects/agent_action_proto.proto",
    package="communicator_objects",
    syntax="proto3",
    serialized_options=_b("\252\002\034MLAgents.CommunicatorObjects"),
    serialized_pb=_b(
        '\n;mlagents/envs/communicator_objects/agent_action_proto.proto\x12\x14\x63ommunicator_objects\x1a\x36mlagents/envs/communicator_objects/custom_action.proto"\x9c\x01\n\x10\x41gentActionProto\x12\x16\n\x0evector_actions\x18\x01 \x03(\x02\x12\x14\n\x0ctext_actions\x18\x02 \x01(\t\x12\x10\n\x08memories\x18\x03 \x03(\x02\x12\r\n\x05value\x18\x04 \x01(\x02\x12\x39\n\rcustom_action\x18\x05 \x01(\x0b\x32".communicator_objects.CustomActionB\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3'
    ),
    dependencies=[
        mlagents_dot_envs_dot_communicator__objects_dot_custom__action__pb2.DESCRIPTOR
    ],
)


_AGENTACTIONPROTO = _descriptor.Descriptor(
    name="AgentActionProto",
    full_name="communicator_objects.AgentActionProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="vector_actions",
            full_name="communicator_objects.AgentActionProto.vector_actions",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text_actions",
            full_name="communicator_objects.AgentActionProto.text_actions",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="memories",
            full_name="communicator_objects.AgentActionProto.memories",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="communicator_objects.AgentActionProto.value",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="custom_action",
            full_name="communicator_objects.AgentActionProto.custom_action",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=142,
    serialized_end=298,
)

_AGENTACTIONPROTO.fields_by_name[
    "custom_action"
].message_type = (
    mlagents_dot_envs_dot_communicator__objects_dot_custom__action__pb2._CUSTOMACTION
)
DESCRIPTOR.message_types_by_name["AgentActionProto"] = _AGENTACTIONPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentActionProto = _reflection.GeneratedProtocolMessageType(
    "AgentActionProto",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AGENTACTIONPROTO,
        __module__="mlagents.envs.communicator_objects.agent_action_proto_pb2"
        # @@protoc_insertion_point(class_scope:communicator_objects.AgentActionProto)
    ),
)
_sym_db.RegisterMessage(AgentActionProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
