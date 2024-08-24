from project import type_of_operation, select_stock, select_ratio
from ratios import pft, lvg, lqd, ROE
from unittest.mock import Mock, patch


def test_type_of_operation():
    with patch('builtins.input', new=Mock(return_value='a')):
        assert type_of_operation() == 'a'
    with patch('builtins.input', new=Mock(return_value='b')):
        assert type_of_operation() == 'b'


def test_select_stock(monkeypatch):
    with patch('builtins.input', new=Mock(return_value='aapl')):
        assert select_stock('a') == 'aapl'

    inputs = iter(['aapl', 'msft'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result_1, result_2 = select_stock('b')
    assert result_1, result_2 == 'aapl, msft'


def test_select_ratio(monkeypatch):
    input = iter(['a'])
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    result = select_ratio('aapl', 'msft')
    assert result == pft('aapl', 'msft')

    input = iter(['c'])
    monkeypatch.setattr('builtins.input', lambda _: next(input))
    result = select_ratio('aapl', 'msft')
    assert result == ROE('aapl', 'msft')
