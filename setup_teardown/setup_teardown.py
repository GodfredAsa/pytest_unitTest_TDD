
class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup Class")

    @classmethod
    def teardown_class(cls):
        print("Teardown Class")


def setup_module(module):
    print("setup module")


def teardown_module(module):
    print("tear down module")


def setup_function(function):
    if function == test_1:
        print("\nsetting up test 1")
    elif function == test_2:
        print("\nsetting up test 2")
    else:
        print("\nsetting up unknown test")


def teardown_function(function):
    if function == test_1:
        print("\nTearing down test 1")
    elif function == test_2:
        print("\nTearing down test 2")
    else:
        print("\nTearing down unknown test")


def test_1():
    print("Executing test1")
    assert True


def test_2():
    print("Executing test2")
    assert True
