str = input()
for i in str:
    print(i.lower() if i.isupper() else i.upper(), end='')