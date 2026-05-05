employees = [
{"id": 1, "name": "Aarav", "dept": "Engineering", "salary": 75000, "experience": 4},
{"id": 2, "name": "Bhavna", "dept": "Sales", "salary": 55000, "experience": 2},
{"id": 3, "name": "Charan", "dept": "Engineering", "salary": 90000, "experience": 6},
{"id": 4, "name": "Divya", "dept": "HR","salary": 48000, "experience": 3},
{"id": 5, "name": "Eswar", "dept": "Engineering", "salary": 120000, "experience": 8},
{"id": 6, "name": "Farah", "dept": "Sales", "salary": 65000, "experience": 5},
{"id": 7, "name": "Gokul", "dept": "HR", "salary": 52000, "experience": 4},
{"id": 8, "name": "Hema", "dept": "Engineering", "salary": 85000, "experience": 5},
]

# apply hike
def apply_hike(employees, percentage):
    hike_cal = list(map(
            lambda employees: {**employees, 
            "salary": employees["salary"] + (employees["salary"] * percentage / 100)}, 
            employees
        )
    )
    return hike_cal

# print(apply_hike(employees, 10))

# bonus check
def eligible_for_bonus(employees):
    return list(filter(
        lambda emp: emp["experience"] >= 5 and emp["salary"] < 100000,
        employees
    ))

# print(eligible_for_bonus(employees))

# sum all salary
from functools import reduce

def total_salary(employees):
    return reduce(
        lambda acc, emp: acc + emp["salary"], 
        employees, 
        0
    )

# print(total_salary(employees))

# group by deparment
def group_by_department(employees):
    unique_dept = set(emp["dept"] for emp in employees)

    group_emp = {
        dept: [emp["name"] for emp in employees if emp["dept"] == dept]
        for dept in unique_dept
    }
    return group_emp

# print(group_by_department(employees))

# ----------5
# highest earning employees

# ----------6
# 
