s = input()
substr = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        str = s[i:j+1]
        substr.add(str)
print(len(substr))