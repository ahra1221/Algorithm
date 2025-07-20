def solution(todo_list, finished):
    answer = []
    for idx in range(len(finished)):
        if not finished[idx]:
            answer.append(todo_list[idx])
    return answer