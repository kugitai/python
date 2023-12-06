'''
a
b
c
'''
a = input()
b = int(input())
c = int(input())
if a == '+':
    print(b+c)
if a == '-':
    print(b-c)
if a == '*':
    print(b*c)
if a == '/':
    if c ==0:
        print('0ではわれません')
    else:
        print(b/c)
