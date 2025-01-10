from employee import Employee

def test_give_default_raise():
    first_employee = Employee('nova', 'rizkiyah', 100000)
    first_employee.give_raise()
    assert first_employee.salary == 105000
def test_give_custom_raise():
    first_employee = Employee('nova', 'rizkiyah', 100000)
    first_employee.give_raise(10000)
    assert first_employee.salary == 110000