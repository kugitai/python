num = int(input())
sosuu_l = []
kekka_l = []
x = 0
if num <= 1:
    print("その数は素因数分解できません")
    quit()
for i in range(2,num+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        sosuu_l.append(i)

while True:
    if num % int(sosuu_l[x]) != 0:
        x+=1
    else:
        num//=int(sosuu_l[x])
        kekka_l.append(sosuu_l[x])
        x = 0
        continue
    if num == 1:
        break
print(sosuu_l)
print(kekka_l)