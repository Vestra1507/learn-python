#Function
def Music(no):
    if no==1:
        print("Open music")
    elif no==2:
        print("Close music")
    elif no==3:
        print("Next music")
    else:
        print("Error")

def Sayhello(time,Username,Age): #user is a parameter
    print("Hello",time,Username)
    print("Age : ",Age)

def saveEmployee(name,dept,salary):
    print(f"ชื่อ {name} แผนก {dept}")
    print(f"เงินเดือน {salary}")




age=15
Sayhello("Morning","Vistra",age) #Argument


saveEmployee("Rachata","Purchasing","25K")
