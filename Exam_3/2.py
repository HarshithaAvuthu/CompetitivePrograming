def Parenthesis(n):
    ans = []
    def recurs(S = '', left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append(S)
            return
        if left < n:
            recurs(S+'(', left+1, right)
        if right < left:
            recurs(S+')', left, right+1)

    recurs()
    # print(ans)
    return (ans,len(ans))



print(Parenthesis(2))
print(Parenthesis(3))
print(Parenthesis(5))
print(Parenthesis(4))
print(Parenthesis(2))
print(Parenthesis(6))