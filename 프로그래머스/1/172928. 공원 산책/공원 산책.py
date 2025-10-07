def solution(park, routes):
    row = len(park)
    col = len(park[0])
    dirs = {
        "N": (-1,0),
        "S": (1,0),
        "W": (0,-1),
        "E": (0,1),
    }
    
    found = False
    for r in range(row):
        for c in range(col):
            if park[r][c] == "S":
                sr,sc = r,c
                found = True
                break
        if found:
            break
    
    def check_route(a,b,c,d,n):
        for i in range(1,n+1):
            nr,nc=a+c*i,b+d*i
            if 0<=nr<row and 0<=nc<col and park[nr][nc] != "X":
                continue
            else:
                return False
        return True
    
    for route in routes:
        op, n = route.split()
        dr,dc = dirs[op]
        if check_route(sr,sc,dr,dc,int(n)):
            sr,sc = sr+dr*int(n), sc+dc*int(n)
    
    return [sr,sc]