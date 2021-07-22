import random

str1="qjsahfoaduvrvbr$&*6#@!~`$%@$^^&GDNGNDn"

chosen=random.sample(str1,23)
pwd="".join(chosen)

print(pwd)

lst=[i for i in str1]

print(lst)

random.shuffle(lst)
print(lst)