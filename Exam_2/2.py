def reconstructQueue(people):

        people = sorted(people, key=lambda x: (x[0],-x[1]))
        # print (people)
        lst = []
        for person in people[::-1]:
            # print(person)
            lst.insert(person[1],person)
            # print (lst)
        return lst



people1=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(reconstructQueue(people1))
people2=[[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]
print(reconstructQueue(people2))
people3=[ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]
print(reconstructQueue(people3))