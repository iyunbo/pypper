from pypper.io.json import deserialize, jsonize, serialize


def test_json_ser_and_deser_on_simple_obj():
    @jsonize
    class MyClass:
        def __init__(self):
            self.prop1 = 1
            self.prop2 = "hello"
            self.prop3 = [1.2, 3.1]

    obj = MyClass()
    serialized = serialize(obj)
    assert serialized == '{"class": "MyClass", "data": {"prop1": 1, "prop2": "hello", "prop3": [1.2, 3.1]}}'
    deserialized = deserialize(serialized)
    assert serialize(deserialized) == serialized


def test_json_ser_and_deser_on_required_arguments():
    @jsonize
    class MyClass:
        def __init__(self, prop1, prop2, prop3):
            self.prop1 = prop1
            self.prop2 = prop2
            self.prop3 = prop3

    obj = MyClass(1, "hello", [1.2, 3, 1])
    serialized = serialize(obj)
    assert serialized == '{"class": "MyClass", "data": {"prop1": 1, "prop2": "hello", "prop3": [1.2, 3, 1]}}'
    deserialized = deserialize(serialized)
    assert serialize(deserialized) == serialized


def test_json_ser_and_deser_on_kwargs_constructor():
    @jsonize
    class MyClass:
        def __init__(self, prop1=None, prop2=None, prop3=None):
            self.prop1 = prop1
            self.prop2 = prop2
            self.prop3 = prop3

    obj = MyClass(prop1=1, prop2="hello")
    serialized = serialize(obj)
    assert serialized == '{"class": "MyClass", "data": {"prop1": 1, "prop2": "hello", "prop3": null}}'
    deserialized = deserialize(serialized)
    assert serialize(deserialized) == serialized


def test_json_ser_and_deser_on_vargs():
    @jsonize
    class MyClass:
        def __init__(self, *props):
            self.props = list(props)

    obj = MyClass(1, "hello")
    serialized = serialize(obj)
    assert serialized == '{"class": "MyClass", "data": {"props": [1, "hello"]}}'
    assert serialize(MyClass(1, None, ["hello"])) == '{"class": "MyClass", "data": {"props": [1, null, ["hello"]]}}'
    deserialized = deserialize(serialized)
    assert serialize(deserialized) == serialized


def test_json_ser_and_deser_on_kwargs():
    @jsonize
    class MyClass:
        def __init__(self, **kwargs):
            self.props = kwargs

    obj = MyClass(prop1=1, prop2="hello")
    serialized = serialize(obj)
    assert serialized == '{"class": "MyClass", "data": {"props": {"prop1": 1, "prop2": "hello"}}}'
    deserialized = deserialize(serialized)
    assert serialize(deserialized) == serialized


def test_json_ser_and_deser_on_modified_property():
    @jsonize
    class MyClass:
        def __init__(self, **kwargs):
            self.props = kwargs

    obj = MyClass(prop1=1, prop2="hello")
    # pylint: disable=attribute-defined-outside-init
    obj.prop2 = "world"
    serialized = serialize(obj)
    assert serialized == '{"class": "MyClass", "data": {"props": {"prop1": 1, "prop2": "hello"}, "prop2": "world"}}'
    deserialized = deserialize(serialized)
    assert serialize(deserialized) == serialized
