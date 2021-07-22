from datetime import datetime

now=datetime.now()

print(now)
n1=now.strftime("Today is %A, %B %d, %Y")

print(n1)