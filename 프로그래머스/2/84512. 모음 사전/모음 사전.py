from itertools import product

def solution(word):
    answer = 0
    moeum = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        for j in product(moeum, repeat=i):
            words.append(''.join(j))
    words.sort()
    return words.index(word) + 1