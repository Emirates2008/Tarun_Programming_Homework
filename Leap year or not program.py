a=int(input("enter a year"))
if (a%4==0):
    if (a%100==0 and not a%400 == 0  ):
        print("This year is not a leap year")
    else:
        if a%400==0:
            print("This year is a leap year")
        else:
            print("This year is not a leap year")
else:
    print("This year is not a leap year")
