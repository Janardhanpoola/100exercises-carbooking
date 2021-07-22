
import pandas

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                    {"firstName": "Anna", "lastName": "Smith"},
                    {"firstName": "Peter", "lastName": "Jones"}],
    "owners":[{"firstName": "Jack", "lastName": "Petter"},
              {"firstName": "Jessy", "lastName": "Petter"}]
    }

d["employees"].append({"fname":"JP","lname":"Poola"})

df=pandas.DataFrame()
df=df.append(d,ignore_index=True)
df.to_json("smple.json")

###########


        