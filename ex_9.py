import requests
     
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)

#print(r.text[:100])
print(r)


##############


r = requests.get('https://api.github.com/users/naveenkrnl') 
  
# check status code for response received 
# success code - 200 
print(r) 
  
# print content of request 
print(type(r.content) )