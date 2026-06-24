# #deep string
# fname = "Rachata "
# Lname = " Sangeamjai "

# fullname = fname+Lname +" Student"
# print(fullname)

# #String หลายบรรทัด
# address = """
# 99/1 moo.7
# Thubma Muang
# Rayong 
# 21000
# Thailand
# """

# print(address)

# # use f if want to use data from variable
# year = 2545
# salary=25000
# message=f"เกิดเมื่อปี พ.ศ. {year}"
# age =f"ปีนี้คุณมีอายุ{2569-year} ปี"
# data=f"your salary is {salary:.5f} บาท"
# print(message)
# print(age)
# print(data)

# #number of variable
# text="HelloPython"
# print(len(text))
# # for c in text:
# #     print(c)
# print(text[0:5])

# #Function of string
# name1 = "Mr.Rachata"
# surname = "Sangeamjai"
# # print(name1.upper())
# # print(name1.lower())
# print(name1.startswith("Mr")) #check คำขึ้นต้น

# name=input("name : ")
# if name.startswith("นาย"):
#     print("male")
# elif name.startswith("นางสาว"):
#     print("Female")

# month = input("Month :")

# if month.endswith("คม"):
#     print("มี 31 วัน")
# elif month.endswith("ยน"):
#     print("มี 30 วัน")

# text = "สวัสดี คุณป้า คุณตา คุณน้า คุณยาย"
# print(text.find("Pyython"))
# print(text.count("o"))
# print(text.count("z"))
# print(text.count("คุณ"))

# # Replace string
# text = "สัญญาจ้างงานประจำปี 2567 มีผลตั้งแต่ มกราคม 2567 ถึง ธันวานคม 2567"
# update = text.replace("2567","2568")
# print(update)

# #delete space
# text = " python ".strip()
# print(len(text))

text="ฉันขื่อ {0} อายุ {1} ปี".format("พี",23)
print(text)


