"""
  This is the program of our chatbot.
  1. The bot will welcome a person to a hotel and ask for his/her name.
  2. It will provide the menu of recipes according to the time he arrived and takes his order.
  3. It also provides the menu of beverages.
  4. It calculates the bill and provides a link to pay.
  5. Finally, it asks for the feedback of the customer.
"""
from datetime import datetime
from Menu import menu,beverages
from Calculate import calculate
from Payment_Feedback import payment,feedback
from Beverages import calculatebev
def welcome():
    time=datetime.now().hour
    if(time>=23 or time <6):
        print("Sorry! The service is not available...\nVisit again...")
        quit()
    greet="Morning"
    if(time>11 and time<16):
        greet="Afternoon"
    elif(time>=16 and time<23):
        greet="Evening"
    return greet
def greeting(name):
    print("\nHi! "+name.upper()+".\nSo nice to see you here.\nHope you will feel easy using me - 'the bot' of LILAC - Volta.\n")
    print("Here's the menu we offer in this time.")
print("\nGood "+welcome()+" !\nWelcome to LILAC - Volta Hotel.")
print("\nMention your name please : ")
name= input()
greeting(name)
menu()
print("You can type the recipe you wish to have in the format\n\nID of the recipe - Quantity(number of plates)\n\nMention one item each time. ")
print("After completing type 'done' .")
calculate()
print("Do you like to have beverages?? \nType 'yes' if you need else type 'no' .")
while(True):
    wish=input()
    if(wish=="yes"):
        print("You can type the beverage you wish to have in the format\n\nID of the beverage - Quantity(number of items)\n\nMention one item each time. ")
        beverages()
        calculatebev()
        break
    elif(wish=="no"):
        print("That's ok...")
        break
    else:
        print("Enter your choice in 'yes' or 'no' .")
payment()
feedback()