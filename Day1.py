# print("Hello world") # show Hello World
# age = int(input("Age = ")) 

# # Check age
# if age > 20: #Logic that check age less than 20 then show Woman but it flase just show Girl 
#     print("Woman")
# else:
#     print("Girl")

#learn about type of data
# name = "Rachata"
# Age = 23
# Grade = 3.5
# Status = True

# # Define variable in 1 
# name,Age,Grade,Status = "Rachata",24,4,True

# # Show data
# print("ชื่อ : ",name)
# print("อายุ : ปี",Age)
# print("เกรด : ",Grade)
# print("สถานะ : ",Status)

#Show type of data
# print(type(name))
# print(type(Age))
# print(type(Grade))
# print(type(Status))
# print(type(4.25))

# # Learn Input Data
# name = input("Name : ")
# born_year = input("year : ")

# print(name)
# print(type(name))
# print(born_year)
# print(type(born_year))

#Learn to covert data
# name = input("Name : ")
# born_year = input("year : ")

# print(name)
# print(born_year)
# print("Age = ",2026-int(born_year),"Year olds")

# print(type(name))
# print(type(int(born_year)))

# #Learn math Opertor / comparision / logic
# n1,n2=2,7

# print("number 1 : ",n1)
# print("number 2 : ",n2)

# #add
# print("sum of n1 and n2 :",n1+n2)
# print("Difference of n1 and n2 :",n2-n1)
# print("multiple of n1 and n2 :",n2*n1)
# print("power of n1 and n2 :",n2**n1)
# print("Divied of n1 and n2 :",n2/n1)
# print("number of divied n1 and n2 :",n2//n1)
# print("Divied of n1 and n2 :",n2%n1)

# #Learn define value
# x,y=2,7

# print("x : ",x)
# print("y : ",y)

# x+=y #x=x+y
# x-=y #x=x-y
# x*=y #x=x*y
# x**=y #x=x**y
# x/=y #x=x**y

# print(x)

# #Comparition condition
# x,y=100,50

# print(x==y) 
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)

# #Logic of if
# Score = int(input("score : "))
# print(Score)
# print(type(Score))

# if Score < 0:
#     print("Invalid")
# elif Score >= 50:
#     print("Grade A")
# else:
#     print("Grade F")

# #Ternary operation
# number = int(input("score : "))
# if number%2==0:
#     print("Odd")
# else:
#     print("Even")

# print("Odd") if number%2==0 else print("Even")

# #Logical Operators
# user = input("user :")
# Pass = input("Password :")
# if user=="admin" and Pass=="1234":
#     print("Log in")
# else:
#     print("Invalid ID")

# #Project 1 analysis student grade
# score = int(input("Score :"))
# grade=None

# if score>=80 and score<=100:
#     grade ="A"
# elif 70<=score<=79:
#     grade ="B"
# elif 0<=score<=69:
#     grade ="C"
# else:
#     grade ="Invalid"

# # output  
# print(grade)

# #Nested if
# user = input("user :")
# Pass = input("Password :")
# if user=="admin" and Pass=="1234":
#     print("Log in")
#     service = int(input("service number :"))
#     if service==1:
#         print("withdraw")
#     elif service==2:
#         print("Pay out")
#     else:
#         print("Invalid service")
# else:
#     print("Invalid ID")

#Match statement
service = input("service : ")
match service:
    case "1":print("ถอนเงิน1")
    case "2":print("ฝากเงิน1")
    case "3":print("ยอดเงินคงเหลือ")
    case "":print("ผิดพลาด") 






