def bincnt(n):
    z = "{0:b}".format(n)
    # print(z)
    k = [i for i, e in enumerate(list(z)) if e == "1"]
    m = 0

    for i in range(len(k)-1):
        if (k[i+1] - k[i]) >0:
            if m < k[i+1] - k[i]:
                m = k[i+1] - k[i]
    print (m)






# bincnt(22)
bincnt(0)
bincnt(55)
bincnt(-5)
bincnt(12354)
bincnt(6)
bincnt(256)