def solution(arr):
    answer = []
    
    quad = []
    def quadtree(x,y,size):
        if size == 1:
            quad.append(arr[x][y])
            return
        
        first = arr[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if first != arr[i][j]:
                    half = size//2
                    quadtree(x,y,half)
                    quadtree(x+half,y,half)
                    quadtree(x,y+half,half)
                    quadtree(x+half,y+half,half)
                    return
        quad.append(first)
    
    quadtree(0,0,len(arr))
    
    zero = 0
    one = 0
    for q in quad:
        if q: one += 1
        else: zero += 1
    answer = [zero,one]
        
    return answer