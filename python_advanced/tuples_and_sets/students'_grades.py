n = int(input())
students = {}
for i in range(n):
    name, grade = input().split()
    str_grade = grade
    grade = float(grade)
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)
for key, value in students.items():
    v = [f'{i:.2f}' for i in value]
    print(f"{key} -> {' '.join(v)} (avg: {sum(value)/len(value):.2f})")
