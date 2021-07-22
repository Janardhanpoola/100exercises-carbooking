with open("new_coun.txt") as f:
    content=f.readlines()
    content=[i.strip("\n") for i in content]
    #print(content)
    checklist = ["Portugal", "Germany", "Munster", "Spain"]
    checked=[i for i in content if i in checklist]
    print(checked)   


###############################


import pandas as pd 

lst=[[1,2,3],[4,5,6]]

df=pd.DataFrame(lst)

#print(df)

#########

import pandas as pd 

nd={'Name':{'firstname':'mohan','lastname':'krishna'},'gender':'male'}

df=pd.DataFrame(nd)

print(df)

##################


import pandas as pd 

list1 = [ 
        { 
        "Student": [{"Exam": 90, "Grade": "a"}, 
                    {"Exam": 99, "Grade": "b"}, 
                    {"Exam": 97, "Grade": "c"}, 
                   ], 
        "Name": "Paras Jain"
        }, 
        { 
        "Student": [{"Exam": 89, "Grade": "a"}, 
                    {"Exam": 80, "Grade": "b"} 
                   ], 
        "Name": "Chunky Pandey"
        } 
       ] 


rows=[]
for data in list1:
    Stu_perf=data['Student']
    name=data['Name']
    print(Stu_perf)

    for row in Stu_perf:
        row['Name']=name
        rows.append(row)

res=pd.DataFrame(rows)




