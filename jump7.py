for d in range(1,101):
    if d % 7 == 0:
        continue
    elif d % 10 == 7:
        continue
    elif d // 10 == 7:
        continue
    else:
        print (d)

