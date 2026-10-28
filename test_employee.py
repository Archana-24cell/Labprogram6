from employee import employee_details


def test_employee_details():
    result = employee_details("Archana", "EMP101", "IT", "30000")

    expected = "Employee Name: Archana\nEmployee ID: EMP101\nDepartment: IT\nSalary: 30000"

    assert result == expected
