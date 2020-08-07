import inspect
import json
from typing import Any, Type

KEY_DATA = "data"
KEY_CLASS = "class"
NAME_SELF_ARGUMENT = "self"

__registry = {}


def jsonize(klass: Type[Any]) -> Type[Any]:
    """
    Use this class decorator to enable the json serialization and deserialization
    :rtype: the decorated class
    """
    __register_class(klass)
    return klass


def serialize(obj: object) -> str:
    """
    Serialize the object into json string
    :param obj: the object
    :return: json string
    """
    return json.dumps(
        {
            KEY_CLASS: obj.__class__.__name__,
            KEY_DATA: obj.__dict__
        }
    )


def __register_class(target_class: Type[Any]):
    __registry[target_class.__name__] = target_class


def deserialize(json_str: str) -> object:
    """
    Covert the json string back to object
    :param json_str: the json string
    :return: the constructed object
    """
    data = json.loads(json_str)
    name = data[KEY_CLASS]
    target_class = __registry[name]
    inputs = data[KEY_DATA]
    obj = __create_object(target_class)
    for key in inputs:
        setattr(obj, key, inputs[key])
    return obj


def __create_object(target_class: Type[Any]) -> object:
    sig = inspect.signature(target_class.__init__)
    pos_args_length = len(
        [param for param in sig.parameters.values() if param.name is not NAME_SELF_ARGUMENT and
         param.kind in (param.POSITIONAL_ONLY, param.VAR_POSITIONAL, param.POSITIONAL_OR_KEYWORD)])
    if pos_args_length > 0:
        default_args = [None] * pos_args_length
        obj = target_class(*default_args)
    else:
        obj = target_class()
    return obj
