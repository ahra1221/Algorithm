from functools import cmp_to_key

def solution(numbers):
    
    def compare(a,b):
        if a+b > b+a:
            return -1
        elif a+b < b+a:
            return 1
        else:
            return 0
    
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = "".join(numbers)
    
    return "0" if answer[0] == "0" else answer