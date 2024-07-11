grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

exam= {
    'Eric': 99,
    'John': 100
}
def add_grades():
    for values , in grades.items():
        values[1].insert(0)




    # add_grades()

for student in grades:
    if student in exam:
        grades[student].insert(0, exam[student])
    else:
        grades[student].insert(0, None)
        
grades
print(grades)
