
def bal(s):
    open="({["
    stack=[]
    matches=tuple( ( (  '(',')' ) , ('[',']')  ,  ('{','}')  ) )
    if len(s)%2!=0:
        return False
    for paren in s:
        if paren in open:
            stack.append(paren)
        else:
            if len(stack)==0:
                return False
            last_open=stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack)==0

s="[{}"

print(bal(s))
    


