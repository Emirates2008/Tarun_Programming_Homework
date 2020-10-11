############################################################################################################
#There is a class with 2000 students. Class teacher need to  generate random username and passwords to them.
#(length of username and password must be 8 characters) Write a python program to do this. Save the username
#and password as dictionary after generating them. 

import random
import string
login_dict={}


def Function(self,length):
    l=string.ascii_uppercase
    hexnumbers = string.hexdigits
    for i in range(100):
        ugen=''.join(random.choice(l) for i in range(length))
        pgen = ''.join(random.choice(hexnumbers) for i in range(length))
        uname=print("Username: " + ugen)
        pwd = print("Password: " + pgen)
########################################## adding two values to a dictionary
        login_dict[ugen]=pgen
################################################
    print(login_dict)
    


Function(8)




#print("Student " + str(stu) + " has a username of " + str(username) + " and his password is " + str(password) + ".")



