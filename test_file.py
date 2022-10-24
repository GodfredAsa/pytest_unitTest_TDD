import pytest


@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")


@pytest.fixture(scope="module", autouse=True)
def setModule():
    print("\nSetup Module")


@pytest.fixture(scope="module", autouse=True)
def setModule():
    print("\nSetup Module")


@pytest.fixture(scope="module", autouse=True)
def setFunction():
    print("\nSetup Function")
