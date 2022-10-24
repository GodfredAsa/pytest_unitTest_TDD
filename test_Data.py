import pytest


@pytest.fixture(params=[1, 2, 10])
def setupData(request):
    retVal = request.param
    print("\nSetup Return Value: {}".format(retVal))
    return retVal


def test_1(setupData):
    print("\nSetup : {}".format(setupData))
    assert True