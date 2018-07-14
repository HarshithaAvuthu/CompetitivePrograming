def binary(n):
	print(bin(n)[2:])


# def method(n1,n2):
# 	b1=binary(n1)
# 	b2=binary(n2)

# 	for i in b1:
# 		for j in b2:
# 			if i==j:
# 				continue
# 			else:
# 				b1[]
# 				count+=1
# 			

def hammingdistance(n1,n2):
	# print(bin(n1^n2))
	b=bin(n1^n2)
	# print(bin().count('1'))
	return b.count('1')


# n1=1
# n2=4
# print(hammingdistance(n1,n2))

print(hammingdistance(25,30)) 
print(hammingdistance(1,4)) 
print(hammingdistance(100,250)) 
print(hammingdistance(1,30)) 
print(hammingdistance(0,255)) 