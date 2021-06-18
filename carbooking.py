import time
from datetime import date, datetime,timedelta



class Car:
    def __init__(self,model,make,registration_year,type):
        self.model=model
        self.make=make
        self.registration_year=registration_year
        self.type=type



class Customer:

    assign_car_dict={} #this is used to track if any customer books a car..he will be associated with a car he books.

    def __init__(self,name,licenseID,address,phone):

        self.name=name
        self.licenseID=licenseID
        self.address=address
        self.phone=phone
    

    def bookAcar(self,car): #method that helps customer to book a car
        now=datetime.now()
        book_time=now.strftime("%H:%M")
        if car in Manager.cars and car not in list(self.assign_car_dict.values()) :#if someone tries to book a car that doesn't exists in cars list or if a car is already booked by someone then it  throws an error msg to book after some time
            self.assign_car_dict[self.name]=car
            #timechange=datetime.now()+timedelta(hours=2)
            print(f"Booking successful at {book_time}")
            print(self.assign_car_dict)

        else:
            if car in Manager.cars: #if car exists in car database
                timedif=now+timedelta(hours=2) #adding a time frame of 2 hours to the time a customer books a car 
                timechange=timedif.strftime("%H:%M") #filtering the data so that we need only time in HH:MM
                print(f"Requested car is not available to book..Please try again after {timechange}")
            else:
                print("We dont have the requested car model")
    




class Manager:

    cars=[]   

    def add_car(self,car):
        self.cars.append(car)
    
    def view_car(self):
        return self.cars

    def del_car(self,car):
        self.cars.remove(car)
    
    def car_status(self,car):
        #print(Customer.assign_car_dict.values())
        if car in list(Customer.assign_car_dict.values()) : # if a person has already a car booked under his name ..he will given 'assigned' status else 'unassigned'
            return 'assigned'
        else:
            return 'unassigned'

#creating car objects
car1=Car('Thar','Mahindra',2020,'petrol')
car2=Car('Creta','Hyundai',2019,'petrol')
car3=Car('Seltos','Kia',2019,'diesel')
car4=Car('Fortuner','Toyota',2020,'petrol')
car5=Car('Bolero','Mahindra',2018,'diesel')
car6=Car('Swift','Maruthi',2019,'petrol')


#manager object
m=Manager()

#Adding cars
m.add_car(car1.model)
m.add_car(car2.model)
m.add_car(car3.model)
m.add_car(car4.model)
m.add_car(car5.model)


m.del_car(car2.model) #removing 'creta' model

print(m.view_car()) #viewing the cars list after deletion

print(m.car_status(car1.model)) #checking the car status before a customer books

#creating customer objects
c1=Customer('Abhishek',1234,'Hyderabad',90889898)

c2=Customer('Bharat',1233,'Bng',875556)

c3=Customer('Charan',66778,'Lck',875876)

c4=Customer('Rajesh',1233,'KKL',76446)


c1.bookAcar(car1.model)   #prints booking msg.

print(m.car_status(car1.model)) #checking the status after car is booked


c2.bookAcar(car1.model)  # if customer2 tries to book car1 which is already booked by customer1..it throws error msg.

c2.bookAcar(car4.model)

c2.bookAcar('jh') #if cust. tries to book a car which does not exists in car database


c3.bookAcar(car4.model)







        

