def minSwapsCouples(row):
    dictionary={}
    couples=[]
    swaps=0
    l=len(row)

    for i in range(0,l,2):

        keys,values = min(row[i]//2, row[i+1]//2), max(row[i]//2, row[i+1]//2)

        while True: 
            if keys in dictionary:
                
                p=dictionary.pop(keys)
                swaps+=1
                keys,values = min(p, values), max(p, values)
                
            if keys == values:    
                break

            if keys not in dictionary:   
                dictionary[keys]=values
                break

    ld=len(dictionary)
    return swaps+ld


# row=[0,2,1,3]
# print(minSwapsCouples(row))
print(minSwapsCouples([0,2,1,3]))
print(minSwapsCouples([3,2,0,1]))
print(minSwapsCouples([1,3,4,0,2,5]))
print(minSwapsCouples([3,1,5,4,6,2]))
print(minSwapsCouples([3,30,50,90,16,91,65,18,61,58]))
print(minSwapsCouples([1,0]))

print(minSwapsCouples([55,37,19,46,66,32,7,81,33,76,00,28,92,26,99,6,56,29,17,52,90,79,91,83,12,40,82,84,2,21,11,68,98,34,73,10,57,58,64,36]))
print(minSwapsCouples([50,23,76,19,16,70,35,68,41,49,99,71,59,95,89,33,22,7,54,83,24,0,18,64,11,14,77,26,42,21,82,1,97,52,65,79,37,62,60,91,98,4,88,36,51,20,85,90,29,84,93,13,80,6,55,48,2,40,46,81,30,3,94,38,27,31,53,86,32,96,8,58,73,5]))