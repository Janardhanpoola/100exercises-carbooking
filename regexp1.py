import re

test='''
111-111-1112
222.222.2222
444*789*9900
'''

pattern=re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')

matches=pattern.finditer(test)

for m in matches:
    print(m.group(0))


#############################################################


line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'

#print(bool(re.search(r'"0xB0"',line2)))
#print(re.compile(r'[a-z]',line1))

pattern=re.compile(r'[a-zA-Z]+\s+[a-zA-Z]+:\s+(\w+,.{6})')

matches=pattern.finditer(line1)

for m in matches:
    print(m.group(0))

############################################

ip = 'They ate 5 apples and 5 oranges'

m=re.sub(r'5','five',ip)
#print(m)

##########################


matches=re.sub(r'5','five',ip,count=2)

print(matches)

################

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

res=[w for w in items if re.search(r'e',w)]

print(res)

###################################

ip = 'This note should not be NoTeD'

#ind=ip.find('note')

#Replace all occurrences of note irrespective of case with X.

t=re.sub(r'note',"X",ip,flags=re.IGNORECASE)

print(t)

#####################

ip = b'tiger imp goa'

print(bool(re.search(b'at',ip)))

############################


para = '''good start
... Start working on that
... project you always wanted
... stars are shining brightly
... hi there
... start and try to
... finish the book
... bye'''

para=para.split('\n')

res=[i for i in para if not re.search(r'start',i,flags=re.I)]

res=[i[4:] for i in res]

print(res)

# pattern=re.compile(r'start.*',flags=re.I)

# matches=pattern.finditer(para)

# for m in matches:
#     print(m)

####################################

items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']

res=[i for i in items if re.search(r'e',i) and re.search(r'n',i) ]

print(res)

########################

ip = 'start address: 0xA0, func1 address: 0xC0'

res=re.sub(r'0xA0','0000',re.sub(r'0xC0','1111',ip))

print(res)

##################

line1 = 'be nice'
line2 = '"best!"'
line3 = 'better?'
line4 = 'oh no\nbear spotted'

pattern=re.compile(r'^be')

print(bool(re.search(pattern,line4)))

######################
# For the given input string, change only whole word red to brown
words = 'bred red spread credible'

pattern=re.sub(r'\bred','brown',words)

print(pattern)

###################################

#For the given input list, filter all elements that contains 42 surrounded by word characters.

words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']

words=[w for w in words if re.search(r'\B42[a-zA-Z0-9]+',w)]

print(words)

#####################

l='Please enter the nine-digit id as it appears on your color - coded pass-key'

print(re.sub(r'\b-\b','$',l))

print(re.sub(r'\B-\B','%',l))


word = "categorical cat"

print(re.search(r'\bcat\b',word))