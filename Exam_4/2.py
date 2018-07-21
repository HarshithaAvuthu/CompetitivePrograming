def counting(n):
# n=int(input())
    lst=[]
    for i in range(0,n+1):
        n=bin(i)
        count=0
        for j in range(0,len(n)):
            if(n[j]=='1'):
            	count+=1
        lst.append(count)
    print(lst)

counting(15)
counting(16)
counting(1)
counting(25)
counting(5)
counting(6)