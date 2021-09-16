for i in range (210235,210301):
    x=0
    for n in range (2,int(i/2+0.5)+1):
        if i % n == 0:
            x += 1
        else:
            continue
    if x == 4:
        print(i)
    else:
        continue
