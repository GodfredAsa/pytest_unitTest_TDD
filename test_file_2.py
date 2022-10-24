import pytest


@pytest.fixture(scope="module", autouse=True)
def setModule2():
    print("\nSetup Module 2")


@pytest.fixture(scope="class", autouse=True)
def setClass2():
    print("\nSetup Class 2")


@pytest.fixture(scope="function", autouse=True)
def setFunction2():
    print("\nSetup Function 2")


def test1():
    print("\nExecuting IT 1")


def test2():
    print("\nExecuting IT 2")

#  order of execution  => module, class, function tests
