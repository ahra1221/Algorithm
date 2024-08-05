def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        if ans == student1[idx % len(student1)]:
            score[0] += 1
        if ans == student2[idx % len(student2)]:
            score[1] += 1
        if ans == student3[idx % len(student3)]:
            score[2] += 1
            
    for idx, sc in enumerate(score):
        if sc == max(score):
            answer.append(idx+1)
            
    return answer