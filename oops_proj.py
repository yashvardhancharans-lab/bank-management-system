                    ############# BANK MANAGEMENT PROJECT ##################

import json
import random
import string 
from pathlib import Path


class Bank:
    database = Path(__file__).parent / "data.json"
    data=[]
    try:
         
         if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
         else:
             print("no such file exists")      
 
    except Exception as err:
        print(f"An error occured as {err}")
    



    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)




    def CreateAccount(self):
        Info= {
            "name" :input("tell your name:"),
            "age"  :int(input("tell your age:")),
            "E-mail":input("tell your email:"),
            "pin":int(input("tell your 4 number pin:")),
            "accountNo.":Bank.__accountgenerate(),
            "balance":0
        }

        if Info['age']<18 or len(str(Info['pin']))!=4:
            print("Sorry you can't cretae a bank account")

        else:
            print("Successfully created account")    
            for i in Info:
                print(f"{i}:{Info[i]}")
            print("please note down your account number")   

            Bank.data.append(Info)

            Bank.__update()
        
        

    def deposite(self):
        accnumber=input("please tell your account number:")
        pin=int(input("tell your pin number:"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]       #([ { "name": ..., "balance": ... } ]   ← LIST)

        if userdata==False:
            print("No data found")

        else:
            amount=int(input("Enter Amount you want to add:"))
            if amount>15000 or amount<100 :
                print("cant deposit amount mor than 15000 or less than 100 ")
            else:
                userdata[0]['balance'] +=amount                                                #([ { "name": ..., "balance": ... } ]   ← LIST)
                Bank.__update()
                print("Amount deposited succesfully")     





    def withdraw(self):
        accnumber=input("Enter your account number:")
        pin=int(input("Enter your pin number:"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        if userdata==False:
            print("Data not found")

        else:
            print(f"your current account balance is {userdata[0]['balance']}")
            amount=int(input("Enetr Amount you want to withdraw is:"))  
            if amount>userdata[0]['balance']-100:
                print("in sufficient balace")

            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print(f"withdrew succesfully the reamining balnce is {userdata[0]['balance']}")




    def showdetails(self):
        accnumber=input("enter account number :")
        pin=int(input("enter pin number :"))
        
        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        if userdata==False:
            print("Data not found")

        else:
            print("******    Your Detials are as following.  ******\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")    

  


    def updatedetail(self):
        accnumber=input("enter account number :")
        pin=int(input("enter pin number :"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        if userdata==False:
            print("details do not match with data")

        else:
            print("You cant change age and account number and balance")
            print("fill details to change or skip it")

            newdata={
                "name":input("name change or skip by enter:"),
                "E-mail":input("tell new email or skip it:"),
                "pin":input("tell new pin or skip it:"),
                "age":input("Tell new age or skip it")
            }

            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["E-mail"]=="":
                newdata["E-mail"]=userdata[0]['E-mail']
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']   
            if newdata["age"]=="":
                newdata["age"]=userdata[0]['age']   
   
            newdata["accountNo."]=userdata[0]['accountNo.']      
            newdata["balance"]=userdata[0]['balance'] 

            if type(newdata["pin"])==str:
                newdata["pin"]=int(newdata["pin"])
            if type(newdata["age"])==str:
                newdata["age"]=int(newdata["age"])   


            for i in newdata:
                if userdata[0][i]==newdata[i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]    

            Bank.__update()
            print("Detials changed successfully")



        
    def delete(self):
        accnumber=input("tell your account number:")
        pin=int(input("tell your pin number:"))

        userdata=[i for i in Bank.data if i["accountNo."]==accnumber and i["pin"]==pin ] 
        
        if userdata==False:
            print("Account not found")

        else:
            check=input("press Y for deleting account or press N for not deleting") 
            if check=='N' or check=='n':
                print("Account not deleted")   
            elif check=='Y' or check=='y':
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account deleted Successfully") 

    

user =Bank()

print("press 1 for creating account")
print("press 2 for depositing money in bank account")
print("press 3 for withdrawing money from account")
print("press 4 for details")
print("press 5 for updating details")
print("press 6 for deleting your account")

check=int(input("Tell your response:- "))

if check==1:
    user.CreateAccount()


if check==2:
    user.deposite()


if check==3:
    user.withdraw()


if check==4:
    user.showdetails()


if check==5:
    user.updatedetail()


if check==6:
    user.delete() 