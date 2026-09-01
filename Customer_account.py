import random
import time
class customeraccount:
    def __init__(self,fullname,email_address,phonenumber,age):
        if fullname=="":
            print("fullname cannot be empty")
            return
        if "@" not in email_address:
            print("Invalid email address")
            return
           
        if phonenumber=="":
            print("Phonenumber cannot be empty")
            return
        if age<=0:
            print("Age must be no zero")
            return
        self.__fullname=fullname
        self.__email_address=email_address
        self.__phonenumber=phonenumber
        self.__age=age
        self.__email_verified=False
        self.__phone_verified=False
        self.__email_otp=None
        self.__phone_otp=None
        self.__email_otp_time=None
        self.__phone_otp_time=None
        self.__balance=0
        self.transaction_history=[]
    def get_fullname(self):
        return self.__fullname
    def get_email_address(self):
        return self.__email_address
    def get_phonenumber(self):
        return self.__phonenumber
    def get_age(self):
        return self.__age
    def get_balance(self):
        return self.__balance
    def set_fullname(self,fullname):
        self.__fullname=fullname
    def set_age(self,age):
        if age>0:
            self.__age=age
            print("Age updated succesfully")
        else:
            print("Age must be greater then zero")
        
    def set_phonenumber(self,phonenumber):
        self.__phonenumber=phonenumber
    def set_email_address(self,email_address):
        self.__email_address=email_address
    def sendEmailotp(self):
        self.__email_otp=random.randint(1000,9999)
        self.__email_otp_time=time.time()
        print("Email otp:",self.__email_otp)
        print("Email OTP sent successfully")
    def verifyEmailotp(self,otp):
        if time.time()-self.__email_otp_time>60:
            print("Email OTP Expired")
            return
        if otp==self.__email_otp:
            self.__email_verified=True
            print("email verified succesfully")
        else:
            print("invalid email otp")
    def sendphoneOTP(self):
        self.__phone_otp=random.randint(1000,9999)
        self.__phone_otp_time=time.time()
        print("Phone OTP:",self.__phone_otp)
        print("Phone OTP Sent successfully")
    def verifyphoneOTP(self,otp):
        if time.time()-self.__phone_otp_time>60:
            print("Phone OTP Expired")
            return
        if otp==self.__phone_otp:
            self.__phone_verified=True
            print("phone verified succesfully")
        else:
            print("invalid phone otp")
    def isfullyverified(self):
        if self.__email_verified and self.__phone_verified:
            return True
        else:
            return False
    def deposit(self,amount):
        if not self.isfullyverified():
            print("Account is not fully verified")
            return
        if amount>0:
            self.__balance+=amount
            self.__transaction_history.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self.__balance
            })
            print("amount deposited:",amount)
            print("current balance:",self.__balance)
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if not self.isfullyverified():
            print("Account is not fully verified")
            return
        if amount<=0:
            print("invalid withdrawn amount")
        elif amount>self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
            self.__transaction_history.append({
            "type": "Deposit",
            "amount": amount,
            "balance": self.__balance
            })
            print("amount withdrawn:",amount)
            print("current balance:",self.__balance)
            
        

    def display(self):
        print("Customer1 Details:")
        print("Fullname:",self.__fullname)
        print("Email Address:",self.__email_address)
        print("Phone number:",self.__phonenumber)
        print("Age:",self.__age)
        print("Email verified:",self.__email_verified)
        print("phone verified:",self.__phone_verified)
        print("fully verified:",self.isfullyverified())
        print("Balance:",self.__balance)
    def display1(self):
        print("Customer Details2:")
        print("Fullname:",self.__fullname)
        print("Email Address:",self.__email_address)
        print("Phone number:",self.__phonenumber)
        print("Age:",self.__age)
        print("Email verified:",self.__email_verified)
        print("phone verified:",self.__phone_verified)
        print("fully verified:",self.isfullyverified())
        print("Balance:",self.__balance)
    def print_add_transaction_history(self):
        print("\nTransaction History")
        for transaction in self.__transaction_history:
            print("Type:", transaction["type"])
            print("Amount:", transaction["amount"])
            print("Balance:", transaction["balance"])
            print("--------------------")

        
C1=customeraccount("Venkat","venkat@123.com",9515205359,29)
C2=customeraccount("Rajesh","rajesh@123.com",9701139222,32)
C1.display()
time.sleep(3)
C2.display1()
print()
C1.set_age(36)
print("Updated age:",C1.get_age())
print()
C1.display()

        
C1.sendEmailotp()
email_otp=int(input("Enter email OTP:"))
C1.verifyEmailotp(email_otp)
print()
C1.sendphoneOTP()
phone_otp=int(input("Enter phone otp:"))
C1.verifyphoneOTP(phone_otp)
print()
print("Fully verified:",C1.isfullyverified())

C2.sendEmailotp()
email_otp=int(input("Enter email OTP:"))
C2.verifyEmailotp(email_otp)
print()
C2.sendphoneOTP()
phone_otp=int(input("Enter phone otp:"))
C2.verifyphoneOTP(phone_otp)
print()
print("Fully verified:",C2.isfullyverified())
amount=float(input("Enter deposit amount: "))
time.sleep(3)
C1.deposit(amount)
time.sleep(3)
C1.deposit(9000)
time.sleep(3)
C1.withdraw(90000)
time.sleep(3)
C1.deposit(9000)
time.sleep(3)
print()
C1.display()
print()
C2.deposit(amount)
time.sleep(3)
C2.deposit(900)
time.sleep(3)
C2.withdraw(90)
time.sleep(3)
C2.deposit(9000)
time.sleep(3)
print()
C2.display1()
    
    
