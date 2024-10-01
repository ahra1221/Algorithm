from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user_result = defaultdict(set)
    report_result = defaultdict(int)
    for i in report:
        a, b = i.split()
        user_result[a].add(b)
        report_result[b] += 1
    
    for i in id_list:
        result = 0
        for j in user_result[i]:
            if report_result[j] >= k:
                result += 1
        answer.append(result)
    return answer