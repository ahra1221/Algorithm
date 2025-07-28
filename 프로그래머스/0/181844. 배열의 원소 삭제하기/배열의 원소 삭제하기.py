def solution(arr, delete_list):
    answer = []
    for a in arr:
        if not a in delete_list:
            answer.append(a)
    return answer