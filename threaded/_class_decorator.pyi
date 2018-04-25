import typing

PY3: bool

class BaseDecorator:
    __wrapped__: typing.Optional[typing.Callable] = ...
    def __init__(self, func: typing.Optional[typing.Callable]=...) -> None: ...
    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...