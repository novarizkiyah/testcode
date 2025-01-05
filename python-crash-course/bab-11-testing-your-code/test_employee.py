from employee import Employee

def test_give_default_raise():
    employee = Employee('Nova', 'Rizkiyah', 100000)
    employee.give_raise()
    assert employee.salary == 105000
def test_give_custom_raise():
    employee = Employee('Nova', "Rizkiyah", 100000)
    employee.give_raise(10000)
    assert employee.salary == 110000
