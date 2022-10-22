
def fizz_buzz(value: int):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)


def isMultiple(value, mod):
    return (value % mod) == 0


def checkFizzBuzz(value, expected):
    actual = fizz_buzz(value)
    assert actual == expected

# ================= TEST CASES BELOW ===================
def test_returns_1_when_1_passed() -> None:
    checkFizzBuzz(1, "1")


def test_returns_2_when_2_passed() -> None:
    checkFizzBuzz(2, "2")


def test_returnsFizz_when_3_passed():
    checkFizzBuzz(3, "Fizz")


def test_returnsBuzz_when_5_passed():
    checkFizzBuzz(5, "Buzz")


def test_returnsFizz_when_multiple_of_3_passed():
    checkFizzBuzz(6, "Fizz")


def test_returnsBuzz_when_multiple_of_5_passed():
    checkFizzBuzz(10, "Buzz")


def test_returnsFizzBuzz_when_multiple_of_3_and_5_passed():
    checkFizzBuzz(15, "FizzBuzz")