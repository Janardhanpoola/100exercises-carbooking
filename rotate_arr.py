
arr=[1,2,3,4,5] #51234 -->1
                #45123 -->2

rotate=4

first=arr[-rotate:]

sec=arr[0:-rotate]

first.extend(sec)

print(first)
