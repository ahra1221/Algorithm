def solution(line):
    answer = []
    
    candidate_x = []
    candidate_y = []
    s = set()
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            
            den = a*d - b*c
            if den != 0:
                x = (b*f - e*d) / den
                y = (e*c - a*f) / den
            
            if x == int(x) and y == int(y):
                candidate_x.append(int(x))
                candidate_y.append(int(y))
                s.add((int(x),int(y)))
    
    maxx, minx = max(candidate_x), min(candidate_x)
    maxy, miny = max(candidate_y), min(candidate_y)
    
    for y in range(maxy, miny-1,-1):
        tmp = ""
        for x in range(minx, maxx+1):
            if (x,y) in s: 
                tmp += "*"
            else: tmp += "."
        answer.append(tmp)
    
    return answer