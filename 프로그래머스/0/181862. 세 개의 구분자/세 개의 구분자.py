def solution(myStr):
    answer = []
    myStr = myStr.replace('a','-').replace('b','-').replace('c','-')
    answer = [st for st in myStr.split('-') if st]
    return answer if answer else ["EMPTY"]