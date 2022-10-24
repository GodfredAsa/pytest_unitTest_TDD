from checkout.Checkout import Checkout
import pytest


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout


def test_CanInstantiateCheckout():
    co = Checkout()


def test_CanAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)


def test_CanAddItem(checkout):
    checkout.addItem("a")


def test_CanCalculateTotalPrice(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotalPrice() == 1


def test_GetCorrectTotalPriceWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotalPrice() == 3


def test_CanAddDiscountRule(checkout):
    checkout.addDiscountRule("a", 3, 2)


# @pytest.mark.skip # used to skip a test you do not want to run
def test_applyDiscountRule(checkout):
    checkout.addDiscountRule("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("b")


def test_ExceptionItemWithoutPrice(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")
