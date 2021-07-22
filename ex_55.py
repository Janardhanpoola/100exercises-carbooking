


def bal(s):
    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            current_ele=stack.pop()
            if (current_ele,i) not in matches:
                return False

    return len(stack)==0

s="}"

opening=set("{[(")

matches=set(  ( ('[',']')    ,  ('(',')' )    ,   ('{','}' )  )   ) 

#matches=(    ('[',']')   )
stack=[]


print(bal(s))


######################

l1="hey you"

print(list(enumerate(l1,1)))


class Point:
  
    def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y
  
    def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
        
p1 = Point(3, 4)
p2 = Point(1, 2)
result = p1-p2
print(result.x, result.y)

######################33

lst=[]
if not lst:
    print("yes")
else:
    print("no")