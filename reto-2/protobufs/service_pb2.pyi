from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ["fileName"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    fileName: str
    def __init__(self, fileName: _Optional[str] = ...) -> None: ...

class singleFileResponse(_message.Message):
    __slots__ = ["name", "lastUpdated", "size"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    lastUpdated: str
    size: float
    def __init__(self, name: _Optional[str] = ..., lastUpdated: _Optional[str] = ..., size: _Optional[float] = ...) -> None: ...

class multipleFilesResponse(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[singleFileResponse]
    def __init__(self, files: _Optional[_Iterable[_Union[singleFileResponse, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
