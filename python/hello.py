
c = input()

b = [True if a in c else False for a in ['gep','dev']]
print(b)

if False not in b:
    print(c)
