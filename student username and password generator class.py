############################################################################################################
#There is a class with 2000 students. Class teacher need to  generate random username and passwords to them.
#(length of username and password must be 8 characters) Write a python program to do this. Save the username
#and password as dictionary after generating them. 

import random
import string
#login_dict={}
class std:
    def __init__(self, length):
        self.hi=length
        self.l=string.ascii_uppercase
        self.h = string.hexdigits
        self.car=''.join(random.choice(self.l) for i in range(self.hi))
        self.b=''.join(random.choice(self.h) for i in range(self.hi))
        self.uname=print("Username: " + self.car)
        self.pwd = print("Password: " + self.b)

    def Function(length):    
        for i in range(100):
            self.car= None
            self.b = None
            self.uname = None
            self.pwd = None
########################################## adding two values to a dictionary
            #login_dict.update(uname=self.a, pwd=self.b)
################################################
           # print(login_dict)
r=std
r.Function(8)
    


#Function(8)




#print("Student " + str(stu) + " has a username of " + str(username) + " and his password is " + str(password) + ".")



