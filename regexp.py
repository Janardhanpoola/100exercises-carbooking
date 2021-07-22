import re

text='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

#pattern=re.compile(r'\w.*@.*\.\w{3}')

#or

pattern=re.compile(r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|edu|net)')

matches=pattern.finditer(text)

for m in matches:
    print(m.group(0))