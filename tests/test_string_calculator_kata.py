import pytest
from src.string_calculator_kata import StringCalculator

calculator = StringCalculator()

def test_add_empty_string():    
    assert calculator.Add("") == 0

def test_add_one_number():
    assert calculator.Add("1") == 1

def test_add_one_number_othercases():
    assert calculator.Add("1000") == 1000

def test_add_two_numbers():
    assert calculator.Add("1,2") == 3
