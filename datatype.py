# #list
# product=["กางเกง",99.99,10,True]
# product1=list(("plant",99.10,10,False))
# print(len(product1))
# #edit list
# product[0]="shirt"


# #การเข้าถึงสมาชิก
# print(product[0])

# #Colors
# colors1=["black","red","green","black"]
# colors2=["white","blue","orange"]
# fullcolors=colors1+colors2
# print(fullcolors)
# print(type(fullcolors))

# colors=["red","green","blue","black","white"]
# print(colors[0:3])

# colors=["red","green","blue","black","white"]
# colors.append("brown") #เพิ่ม 1 รายการ
# colors.extend(["orange","yellow"])
# colors.insert(1,"gray")
# colors.remove("blue")
# #colors.clear()
# colors.sort()
# colors.reverse()
# print(colors)

# #Tuple
# product=("plant",150.0,10)
# #(name,price,stock)=product
# # print(product[2])
# # print(product[0])
# # print(len(product))
# #print(price)
# for item in product:
#     print(item)
# colors=("red","green","blue")
# colors2=tuple(("red","black","white"))
# fullcolors=colors+colors2
# # print(fullcolors)
# # print(type(fullcolors))
# # print(len(fullcolors))
# # power=colors*2
# # print(power)
# # print(fullcolors[2:])
# print(colors.index("blue"))
# print(fullcolors.count("red"))

# # #How to use set
# animals={"bird","dog","Lion","tiger",100,True}
# animals.add("duck")
# animals.update(("rabbit","Zebra"))
# pet={"dog","cat","rabbit"}
# # data=animals.union(pet)
# data=animals.difference(pet)
# # print(len(animals))
# # print(type(animals))
# # for item in animals:
# #     print(item)
# # print("frog"in animals)

# print(data)

#Dictionary
colors={
    "red":"แดง",
    "green":"เขียว",
    "blue":"ฟ้า"
}
colors["yellow"]="เหลือง"
colors["blue"]="คราม"

confirms={
    True:"ตกลง",
    False:"ยกเลิก"
}

month={
    1:"มกราคม",
    2:"Feb",
    3:"March"
}

number={
    "เลขคู่":[2,4,6,8,10],
    "เลขคี่":[1,3,5,7,9]
}
# print(colors["green"])
# print(colors["yellow"])
# print(type(colors))
# print(len(colors))
print(number["เลขคู่"])