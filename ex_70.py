def printVowelSum(strs):
    for i in strs:
        print(printVowelCount(i))

def printVowelCount(s):
    count = 0
    vowels = ['a','e','i','o','u']
    
    for i in range(len(s)):
        for j in range(len(s)):
            sub_st = s[i:j+1]
            if(len(sub_st)>0):
                for n in range(len(sub_st)):
                    if sub_st[n] in vowels:
                        count += 1
    return count

printVowelSum(['baceb','xyz','abc'])