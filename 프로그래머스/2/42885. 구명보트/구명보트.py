from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        tmp = people.pop()
        if len(people) > 0 and tmp + people[0] <= limit:
            people.popleft()
        answer += 1
    return answer