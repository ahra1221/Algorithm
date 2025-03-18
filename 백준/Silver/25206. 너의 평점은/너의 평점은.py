i = 0
grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0}

total = 0
sum = 0

while i < 20:
    score = input().split()
    if score[2] != 'P':
        total += float(score[1])
        sum += float(score[1]) * grade[score[2]]
    i += 1

print(sum / total)