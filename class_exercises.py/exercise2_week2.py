#Ask the user to give a year.
#Find if the year the user asked is a leap year or not.
#Display if the year is a leap year or not.


print("find if a year is a leap year ".title())    #Description of the program to the user.

year = int(input("input year!:").title())          #Using input function and int function for the user input.

if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):     #Using the if the command to check different years with the % operator and the formula to find leap years, E.X : if the remainder after the division with 400 is 0 it is a leap year,if the remainder after dividing by 100 is not 0 but still is with 4 its a leap year.
   
    print("this is a leap year!".title())                         
else:                                                               
    print("this is not a leap year!".title())



 


     