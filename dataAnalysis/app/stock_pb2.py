# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: stock.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'stock.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstock.proto\"A\n\rStockRequest1\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\"C\n\x0eStockResponse1\x12 \n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x12.StockResponseData\x12\x0f\n\x07message\x18\x02 \x01(\t\"C\n\rStockRequest2\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\"C\n\x0eStockResponse2\x12 \n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x12.StockResponseData\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xcc\x01\n\x11StockResponseData\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\x10\n\x08\x65xchange\x18\x03 \x01(\t\x12\x10\n\x08turnover\x18\x04 \x01(\t\x12\x0e\n\x06volume\x18\x05 \x01(\t\x12\x11\n\tamplitude\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0f\n\x07highest\x18\x08 \x01(\t\x12\x0e\n\x06lowest\x18\t \x01(\t\x12\x13\n\x0b\x62\x65ijingTime\x18\n \x01(\x03\x12\x11\n\ttimestamp\x18\x0b \x01(\t2j\n\x0cStockService\x12,\n\tGetStock1\x12\x0e.StockRequest1\x1a\x0f.StockResponse1\x12,\n\tGetStock2\x12\x0e.StockRequest2\x1a\x0f.StockResponse2B(\n\x11st.backend.stocksB\x11StockServiceProtoP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stock_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021st.backend.stocksB\021StockServiceProtoP\000'
  _globals['_STOCKREQUEST1']._serialized_start=15
  _globals['_STOCKREQUEST1']._serialized_end=80
  _globals['_STOCKRESPONSE1']._serialized_start=82
  _globals['_STOCKRESPONSE1']._serialized_end=149
  _globals['_STOCKREQUEST2']._serialized_start=151
  _globals['_STOCKREQUEST2']._serialized_end=218
  _globals['_STOCKRESPONSE2']._serialized_start=220
  _globals['_STOCKRESPONSE2']._serialized_end=287
  _globals['_STOCKRESPONSEDATA']._serialized_start=290
  _globals['_STOCKRESPONSEDATA']._serialized_end=494
  _globals['_STOCKSERVICE']._serialized_start=496
  _globals['_STOCKSERVICE']._serialized_end=602
# @@protoc_insertion_point(module_scope)
