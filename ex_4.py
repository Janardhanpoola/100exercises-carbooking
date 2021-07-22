
#Exercise 58 - Add to JSON

# import json

# with open("smple2.json","r") as f:
#     d=json.load(f)

# print(d)

# #d["employees"].append({"fname":"j","lname":"poola"})

# with open("smple2.json","w") as f:
#     json.dump(d,f,indent=4)

#################################

import json

with open('smple2.json',"r") as f:
    d=json.load(f)

print(d)

d['employees'].append({'fname':'j','lname':'poola'})

with open('smple3.json',"w") as f:
    json.dump(d,f,indent=4)  #converting python to json
