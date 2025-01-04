def solution(participant, completion):
    dict = {i:0 for i in participant}
    for i in participant:
        dict[i] += 1
    for j in completion:
        if j in dict:
            dict[j] -= 1
    sorted_dict = sorted(dict.items(), key= lambda item:item[1], reverse=True)
    return sorted_dict[0][0]