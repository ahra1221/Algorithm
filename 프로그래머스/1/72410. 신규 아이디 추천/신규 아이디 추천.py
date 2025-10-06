def solution(new_id):
    answer = ''
    canuse = {"-","_","."}
    pw = new_id.lower() #1단계
    pw = "".join(p for p in pw if p in canuse or p.isalnum()) #2단계
    while ".." in pw: #3단계
        pw = pw.replace("..",".")
    pw = pw.strip(".") #4단계
    pw = pw if pw else "a" #5단계
    if len(pw) >= 16: #6단계
        pw = pw[:15]
    pw = pw.rstrip(".")
    while len(pw) < 3: #7단계
        pw += pw[-1]  
    return pw