import pytest
from src.string_calculator_kata import StringCalculator

@pytest.fixture
def calculator():
    return StringCalculator()

def test_add_empty_string(calculator):    
    assert calculator.Add("") == 0

def test_add_one_number(calculator):
    assert calculator.Add("1") == 1

def test_add_one_number_othercases(calculator):
    assert calculator.Add("1000") == 1000

def test_add_two_numbers(calculator):
    assert calculator.Add("1,2") == 3

def test_add_five_numbers(calculator):
    assert calculator.Add("1,2,3,4,5") == 15

def test_add_twenty_numbers(calculator):
    assert calculator.Add("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20") == 210

@pytest.mark.parametrize("input,expected", [
    ("1\n2,3", 6),
    ("1\n2\n3", 6),
])
def test_should_handle_newlines_between_numbers(calculator, input,expected):
    assert calculator.Add(input) == expected

def test_add_custom_delimiter(calculator):
    assert calculator.Add("//;\n1;2;5") == 8

def test_add_numbers_ignore_above_1000(calculator):
    assert calculator.Add("1001,2") == 2

def test_add_custom_delimiter_any_length(calculator):
    assert calculator.Add("//[***]\n1***2***3***5") == 11
