from datetime import datetime

age=int(input("enter age "))

current_year=datetime.now().strftime("%Y")

born_year=int(current_year)-age

print("we think you born in the year %d"%(born_year))