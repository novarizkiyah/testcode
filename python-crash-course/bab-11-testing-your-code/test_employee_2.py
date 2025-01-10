import pytest
from employee import Employee

@pytest.fixture
def first_employee():
    first_employee = Employee('nova', 'rizkiyah', 100000)
    return first_employee
def test_give_default_raise(first_employee):
    first_employee.give_raise()
    assert first_employee.salary == 105000
def test_give_custom_raise(first_employee):
    first_employee.give_raise(10000)
    assert first_employee.salary == 110000