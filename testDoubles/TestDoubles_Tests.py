import pytest
from pytest import raises

from testDoubles.LineReader import ReadFromFile
from unittest.mock import MagicMock


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returnCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = ReadFromFile("data")
    mock_open.assert_called_once_with("data", "r")
    assert result == "test line"


def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = ReadFromFile("data")

