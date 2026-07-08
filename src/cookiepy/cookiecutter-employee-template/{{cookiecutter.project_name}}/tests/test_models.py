from src.models import Employee

def test_valid_employee():
    emp = Employee(
        id=1,
        name="John",
        email="john@gmail.com",
        age=30,
        salary=50000
    )

    assert emp.age == 30

