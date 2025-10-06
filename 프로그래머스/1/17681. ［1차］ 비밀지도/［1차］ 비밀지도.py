def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        itob = format(i,'b').zfill(n)
        jtob = format(j,'b').zfill(n)
        line = ''.join('1' if x == '1' or y == '1' else '0' for x, y in zip(itob, jtob))
        answer.append(line.replace("1","#").replace("0"," "))
    return answer