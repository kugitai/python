import random
while True:
    inpoint = 0
    allpoint = input('何個の点をおきますか')
    if allpoint == 'end':
        break
    else:
        allpoint = int(allpoint)
        for i in range(allpoint):
            x = random.uniform(0,1)
            y = random.uniform(0,1)
            if x**2+y**2 <= 1.0:
                inpoint+=1
            pi = inpoint*4/allpoint
            print(pi)


