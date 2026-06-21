# #while loop
# x=10
# while x <10:
#     x+=1
#     print(x)
# print("Finish")

# # For loop
# for x in range(0,3,2): #(initial value,Final value,value increase)
#     print(x)
#     print("jub")

# # Break//Continue
# for counter in range(1,10):
#     if counter%2==0:
#         continue
#     print(counter)
# print("Finish")

# # แม่สูตรคูณ
# number = int(input("แม่สูตรคูณ : "))
# for x in range(1,13):
#     print(number,"x",x," = ",number*x)
# print("Finish")

# # sum 5 values
# sum = 0
# for x in range(1,6):
#     number = int(input("ลำดับที่ "+str(x)+" : "))
#     sum = number+sum
# print("sum of 5 values = ",sum)

# # sum of unlimited
# sum = 0
# x=1
# while True :
#     number = int(input("number "+str(x)+" : "))
#     x+=1
#     sum+=number
#     if number==0 or number<0:
#         break
# print("Sum of number : ",sum)

# #nested loop
# for i in range(2):
#     print(i)
#     for j in range(3):
#         print(j)
# print("Finish")

#แม่สูตรคูณแบบกำหนดช่วง
num1 = int(input("Start : "))
num2 = int(input("Finish : "))

for x in range(num1,num2+1):
   # print(x)
    for i in range(1,13):
        print (x," X ",i," = ",x*i)
print("All done") 