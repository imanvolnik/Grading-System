grade_num = int(input("Enter number of grades: "))
grade_lst = []
a_num = 0
b_num = 0
c_num = 0
d_num = 0
f_num = 0

for i in range(grade_num):
    grade = int(input("Enter grade: "))
    grade_lst.append(grade)
    i += 1

for j in range(len(grade_lst)):
    x = grade_lst[j]
    if 90 <= x <= 100:
        a_num += 1
    elif 75 <= x <= 89:
        b_num += 1
    elif 60 <= x <= 74:
        c_num += 1
    elif 50 <= x <= 59:
        d_num += 1
    elif 0 <= x <= 49:
        f_num += 1


def grade_stat(letter):
    if letter == "a":
        print(f"A: {a_num} grades {int((a_num * 100) / len(grade_lst))}%")
    elif letter == "b":
        print(f"B: {b_num} grades {int((b_num * 100) / len(grade_lst))}%")
    if letter == "c":
        print(f"C: {c_num} grades {int((c_num * 100) / len(grade_lst))}%")
    if letter == "d":
        print(f"D: {d_num} grades {int((d_num * 100) / len(grade_lst))}%")
    if letter == "f":
        print(f"F: {f_num} grades {int((f_num * 100) / len(grade_lst))}%")


if grade_num > 1:
    grade_stat("a")
    grade_stat("b")
    grade_stat("c")
    grade_stat("d")
    grade_stat("f")
else:
    if 90 <= x <= 100:
        print(f"{x} - A")
    elif 75 <= x <= 89:
        print(f"{x} - B")
    elif 60 <= x <= 74:
        print(f"{x} - C")
    elif 50 <= x <= 59:
        print(f"{x} - D")
    elif 0 <= x <= 49:
        print(f"{x} - F")
