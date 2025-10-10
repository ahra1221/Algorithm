import re

def solution(files):
    answer = []
    file_part = {}
    for idx, file in enumerate(files):
        head = re.search(r'^\D*',file)
        number = re.match(r'\d+', file[head.end():])
        file_part[file] = [head.group().lower(), int(number.group()), idx]
    print(file_part)
    for k, v in sorted(file_part.items(), key=lambda x:(x[1][0], x[1][1], x[1][2])):
        answer.append(k)
    return answer