#string


# first_name = "Bro"
# food = "Pizza"
# email = 'ausshakirahmed@gmail.com'
# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is  {email}")

# ! integer 

# age = 25;
# quantity = 3;
# print(f"You are {age} years old")
# print(f"You are buying {quantity} items")


# !boolean type 
# is_Student = True
# if is_Student:
#     print("you are a student")
# else:
#     print("You are not a student")


# is_Student2 = False
# if is_Student2:
#     print("you are a student")
# else:
#     print("You are not a student")

#?typescript 
# name= "Bro Code"
# age = 25
# gpa = 3.2
# is_Student = True
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_Student))
# print(name)

# name = input("What is your name?:")
# age = int(input("How old are you?:"))
# age = age+1;
# print(f"Hello {name}!")
# print("Happy birthday")
# print(f"you are {age} years old now")

# item = input("What item would you like to buy?:")
# price = float(input("What is the price of the item?:"))
# quantity = int(input("How many would you like to buy?:"))
# total = price * quantity
# print(f"You have bought {quantity}  {item}")
# print(f"Your total is: ${total}")

# !word games 
# adjective1 = input("Enter an adjective (description):")
# noun1 = input("Enter a noun(person , place , thing)")
# adjective2 = input("Enter an adjective(description):")
# verb1 = input("Enter a verb ending with 'ing")
# adjective3 = input("Enter an adjective(description):")
# print(f"Today i went to a {adjective1} zoo.")
# print(f"In an exhibition, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# import math 
# x = 4 
# y=9
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# print(result)
# result1 = math.ceil(x)
# result2 = math.floor(y)
# print(result1)
# print(result2)

# radious = float(input("Enter the radious of a circle:"))
# circumference = 2*math.pi*radious
# print(f"The circumference is:{round(circumference,2)}")

# age = int(input("Enter your age:"))

# if age >= 18:
#     print("you are now an adult and you can vote now")
# elif age <0:
#     print("You haven't been born yet")

# elif age==0:
#     print("Your age is zero and you are a baby")
# elif age>=100:
#     print("You are very old to give your vote")
# else:
#     print("You must be 18+ to sign na and give your vote")
# *hello world

# !Python calculator
# operator = input("Enter the operator (+,-,*,/):")
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))

# if operator =="+":
#     result = num1 + num2
#     print("The result is :",result)
# elif operator =="-":
#     result = num1 - num2
#     print("The result is :",result)
# elif operator =="*":
#     result = num1 * num2
#     print("The result is :",result)
# elif operator =="/":
#     result = num1 / num2
#     print("The result is :",result)
# else: 
#     print(f"{operator} is not valid operator")


# ! kg to pound convettor 
# weight = float(input("Enter your weight:"))
# unit = input("kilogram or pounds?(kg/lb):")

# if unit =="kg":
#     weight = weight * 2.205;
#     print(f"Your weight in pound is {weight} lb")
#     unit = "lb"
# elif unit == "lb":
#     weight = weight / 2.205;
#     print (f"Your weight in kilogram is {weight} kg")
#     unit = "kg"
# else :
#     print(f"{unit} is not a valid unit") 

# print(f"Your new weight is {round(weight)} {unit}")


# ? kg to pound convertor
# !weight to pound or pound to weight convertor
# * kg to pound convertor calculator
# weight = float(input("Enter your weight:"))
# unit = input("Kilogram or pound?(kg/lb):")

# if unit=="kg":
#     weight = weight * 2.205;
#     print(f"Your weight in pound is {weight} lb")
#     unit ="lb"

# elif unit=="lb":
#     weight = weight /2.205;
#     print(f"Your weight in kilogram is {weight} kg")
#     unit = "kg"

# else:
#     print(f"{unit} is not a valid unit")

# print(f"your new weight is {round(weight)} {unit}")

# list1 = ["apple","banana","Mango"]
# list2 = [1,2,3,4,5]
# list3 = [True,False,True]
# print(type(list1))
# print(type(list2))
# print(type(list3))

# thislist = list(("apple","Banana","cherry"))
# print(thislist)
# thislist2 = list(("apple","Banana","Mango"))
# mainitems =(thislist2)
# print(mainitems[1])

# thislist3 = ["apple","banana","cherry","orange","kiwi","WaterMelon","mango"]
# print(thislist3)
# print(thislist3[2:5])
# print(thislist3[:4])
# print(thislist3[2:])

# print(thislist3[-4:-1])
# if "apple" in thislist3:
#     print("Yes apple is present in the list")

# thislist =["apple","banana","Cherry","Orange","kiwi","mango"]
# print(thislist)
# thislist[1:3]=["blackcurrant","watermelon"]
# print(thislist)


# thislist =["apple","banana","Cherry"]
# print(thislist)
# thislist.insert(2,"watermelon")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)
# thislist = ["apple","banana","cherry"]
# thislist.insert(1,"orange")
# print(thislist)

# tropical = ["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thistuple =("kiwi","orange","evan")
# thislist.extend(thistuple)
# print(thislist)
# thislist.append(thistuple)
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.pop(1)
# print(thislist)
# del thislist[0]
# print(thislist)
# del thislist

# thislist = ["apple","banana","cherry"]
# thislist.clear()
# print(thislist)
# for x in thislist:
#     print(x)
# for x in range(len(thislist)):
#     print(x)
#     print(thislist[x])


# thislist =["apple","banana","cherry"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1

# a = float(input())
# if a<=400.00:
#     a1 =a+a*0.15
#     b1=a1-a
#     print(f"Novo salario: {a1:.2f}")
#     print(f"Reajuste ganho: {b1:.2f}")
#     print(f"Em percentual: {(b1/a)*100:.0f} %")
# elif a>=400.01 and a<=800:
#     a2=a+a*0.12
#     b2=a2-a
#     print(f"Novo salario: {a2:.2f}")
#     print(f"Reajuste ganho: {b2:.2f}")
#     print(f"Em percentual: {(b2/a)*100:.0f} %")
# elif a>=800.01 and a<=1200:
#     a3=a+a*0.10
#     b3=a3-a
#     print(f"Novo salario: {a3:.2f}")
#     print(f"Reajuste ganho: {b3:.2f}")
#     print(f"Em percentual: {(b3/a)*100:.0f} %")
# elif a>=1200.01 and a<=2000:
#     a4=a+a*0.07
#     b4=a4-a
#     print(f"Novo salario: {a4:.2f}")
#     print(f"Reajuste ganho: {b4:.2f}")
#     print(f"Em percentual: {(b4/a)*100:.0f} %")
# else:
#     a5=a+a*0.04
#     b5=a5-a
#     print(f"Novo salario: {a5:.2f}")
#     print(f"Reajuste ganho: {b5:.2f}")
#     print(f"Em percentual: {(b5/a)*100:.0f} %")

# fruits = ["apple","Banana","cherry","kiwi","mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# newlist = [x.upper() for x in fruits]
# newlist.upper(fruits)
# print(newlist)

# thislist = ["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)

# def myfunc(n):
#     return abs(n-50)
# thislist =[100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# list1 = ["a","b","c"]
# list2 = [1,2,3]
# list3 = list1 + list2
# print(list3)

# list1 = ["a","b","c"]
# list2 = [1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1)


# list1 = ["A","b","c"]
# list2 = [1,2,3]
# list1.extend(list2)
# print(list1)

# thistuple =("apple",)
# print(type(thistuple))
# thistuple2 = ("apple")
# print(type(thistuple2))

# tuple1 =("apple",34,True,40,"male")
# print(type(tuple1))

# thistuple =("apple","banana","cherry")
# if "apple" in thistuple:
#     print("Yes, item is present in the tuple")
# else:
#     print("No, The item is not present in the tuple")

# x = ("apple","banana","Cherry")
# print(x)
# y = list(x)
# y.append("orange")
# print(y)

thistuple = ("apple","banana","cherry")
# print(thistuple)
# y = list(thistuple)
# print(y)
# y.remove("banana")
# print(y)
# del thistuple
# print(thistuple)
# for i in range(len(thistuple)):
#     print(thistuple[i])

# i = 0
# while i<len(thistuple):
#     print(thistuple)
#     i=i+1

# tuple1 = (1,2,3)
# tuple1= tuple1 *2
# # print(tuple1)

# thisset = {"apple","banana","cherry",True,1,2} # 1 is considered as same as True
# print(thisset)

# thisset = {"apple","banana","cherry",True,False}
# print(thisset)


# thisset = set(("apple","banana","Cherry"))
# print(thisset)

# thisset = {"apple","Banana","Cherry"}
# print(thisset)
# tropical = {"pineapple","mango","papaya"}
# print(tropical)
# thisset.update(tropical)
# print(thisset)

# thisset = {"apple","banana","Cherry"}
# mylist = ["Kiwi","orange"]
# thisset.update(mylist)
# print(thisset)

# thisset = {"apple","banana","cherry"}
# thisset.discard("banana")
# # print(thisset)
# x =thisset.pop()
# print(x)
# print(thisset)

# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)
# set1.update(set2)
# print(set1)

car = {
    "brand": "Ford",
    "model":"Mustang",
    "year":1964
}
# print(thisdict)
# x = thisdict["model"]
# x = thisdict.get("model")
# print(x)

# x = car.values()
# print(x)
# car["year"]=2020
# print(x)

# x1 = car.items()
# print(x1)


# day = int(input())
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")

# day = int(input("Enter the day:"))
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(*kids):
#     print("The youngest is " +kids[0])
# my_function("Emil","Tobias","Linus")

# def my_function(fname,lname):
#     print(fname + " " + lname)
# my_function("emily","Muna")

# def my_function(*kids):
#     print("the youngest child is " +kids[2])
# my_function("ripa","jidan","Evan")
# class Phone():
#     def call(self):
#         print("You can call by using phone")
#     def message(self):
#         print("You can message by  using the phone")
# class Iphone(Phone):
#     def call(self):
#         print("You can call by using Iphone")
#     def message(self):
#         print("You can message by using the Iphone")
#     def photo(self):
#         print("You can take photo by using the IPhone")
# I = Iphone()
# I.message()
# I.call()
# I.photo()

# print(issubclass(Iphone,Phone))
# print(issubclass(Phone,Iphone))

# p = Phone()
# p.call()
# p.message()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# class Animal():
#     alive = True

#     def eat(self):
#         print("This animal is eating")

#     def sleep(self):
#         print("This animal is sleeping")

# class Rabbit(Animal):
#     pass
# class Fish(Animal):
#     pass
# class Hawk(Animal):
#     pass

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# class Animal():
#     alive = True
#     def eat(self):
#         print("the animal can eat")
#     def sleep(self):
#         print("The animal can sleep")
#     def run(self):
#         print("THe animal can run")
# class Rabbit(Animal):
#     pass
# class Fish(Animal):
#     pass
# class Hawk(Animal):
#     pass

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(Rabbit().alive)
# Fish().eat()
# Hawk().sleep()
# Fish().run()
# Hawk().run()


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# numbers = [1,2,3,4,5]
# numbers =input("enter the numbers:")
# for x in numbers:
#     print(x)    
#     x= x + 1
    
# num = int(input("Enter the numbers:"))
# for i in range(num):
#     print(i)

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("drive!")
    
# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("sail!")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("fly")

# car1 = Car("ford","Mustang")
# boat1 = Boat("Ibiza","Touring 20")
# plane1 =Plane("boeing","747")

# for x in (car1,boat1,plane1):
#     x.move()

# def myfunc():
#     x = 300
#     def myinnerfunc():
#         x=200
#         print(x)
#     myinnerfunc()
#     print(x)
# myfunc()

# x = 300
# def myfunc():
#     global x
#     x = 200
# myfunc()
# print(x)

# def myfunc1():
#     x = "jane"
#     def myfunc2():
#         nonlocal x
#         x ="hello"
#     myfunc2()
#     return x
# print(myfunc1())

# def greeting(name):
#     print("hello, " + name )

# greeting("Evan")

# import datetime
# x = datetime.datetime.now()
# print(x)

# import datetime

# x = datetime.datetime.now()

# # print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%C"))
# print(x.strftime("%D"))

# import json

# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
# y = json.loads(x)
# the result is a Python dictionary:
# print(y["age"])
# print(y)


 
# import json 
# x = '{"name":"John", "age":"30","city":"New York"}'
# y = json.loads(x)  # Convert json to python
# z = json.dumps(y)  #Convert python to json
# print(z)
# print(y)

# import json
# Person = {
#     "name": "Evan Bhai",
#     "age":25,
#     "City": "Dhaka",
#     "Department":"CSE"
# }
# # python dictionary to python string
# Person_json = json.dumps(Person)
# print(Person_json)
# # json string to python dictionary
# Person_python = json.loads(Person_json)
# print(Person_python)

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))

# import json
# person_dict = {"name":"Bob",
#                "langauges":["English","French"],
#                "married":True,
#                "age":25}

# with open('person.txt','w') as json_file:
#     json.dump(person_dict,json_file)
# def check_even(number):
#     if number % 2 == 0:
#           return True  
#     return False
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # if an element passed to check_even() returns True, select it
# even_numbers_iterator = filter(check_even, numbers)
# # converting to list
# even_numbers = list(even_numbers_iterator)
# print(even_numbers)


def c_to_f(temp):
    return (temp * 9/5)+32

celsius_temps =[0.0,18.0,20.0,30.0,40.0,50.0]
fahrenheit_temps = list(map(c_to_f,celsius_temps))
print(fahrenheit_temps)


for temp in fahrenheit_temps:
    print(temp)
def c_to_f(temp):
    return (temp * 9/5)+32

celsius_temps =[0.0,18.0,20.0,30.0,40.0,50.0]
fahrenheit_temps = list(map(lambda temp: (temp * 9/5)+32, celsius_temps))
print(fahrenheit_temps)


















