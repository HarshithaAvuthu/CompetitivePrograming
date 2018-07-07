# def isanagram(s,t):
# 	if anagram(s,t):
# 		return true
# 	else:
# 		return false

def anagram(s,t):
	s=s.lower()
	t=t.lower()
	count=0
	l=len(s)
	for i in s:
		if i in t:
			# return true
			count+=1

	if(count==l):
		return True
	else:
		return False




# s='Dormitory'
# t=''
# print(anagram(s,t))
print(anagram('anagram','nagaram'))
print(anagram('rat','cat'))
print(anagram('keep','peek'))
print(anagram('School Master','The Classroom'))
print(anagram('Mother In Law',' Hitler Woman'))
print(anagram('joy','Enjoy'))
print(anagram('Debit Card','Bad Credit'))
print(anagram('Toss','Shot'))
