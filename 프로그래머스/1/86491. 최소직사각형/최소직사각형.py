def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    for size in sizes:
        size = sorted(size)
        if size[0] > max_width:
            max_width = size[0]
        if size[1] > max_height:
            max_height = size[1]
    return max_width * max_height