count1 = 0
count = 0
count2 = 0
f1 = sum(1 for line in open('1.txt',encoding="utf-8"))
f2 = sum(1 for line1 in open('2.txt',encoding="utf-8"))
f3 = sum(1 for line2 in open('3.txt',encoding="utf-8"))
min_str = min(f1, f2, f3)
max_str = max(f1, f2, f3)

with open('4.txt', 'a',encoding="utf-8") as f:
    f.write('2.txt\n')
    for i in range(min_str):
        count2 += 1
        f.write(f"Строка номер {count2} файла номер 2\n")

    if max_str > f1 > min_str:
        f.write('1.txt\n')
        for i in range(f1):
            count1 += 1
            f.write(f"Строка номер {count1} файла номер 1\n")

    if max_str > f2 > min_str:
        f.write('2.txt\n')
        for i in range(f2):
            count1 += 1
            f.write(f"Строка номер {count1} файла номер 2\n")

    if max_str > f3 > min_str:
        f.write('3.txt\n')
        for i in range(f3):
            count1 += 1
            f.write(f"Строка номер {count1} файла номер 3\n")
    f.write('3.txt\n')
    for j in range(max_str):
        count += 1
        f.write(f"Строка номер {count} файла номер 3\n")