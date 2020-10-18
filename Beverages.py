"""
   This module returns the bill of beverages.
"""
from datetime import datetime
from Menu import hot_beverages,cold_beverages
from Calculate import calculate
import Calculate

# Takes the order and displays the bill of beverages and also the total bill, when the function is called...
def calculatebev():
    total=Calculate.total_bill
    orders={}
    while(True):
        input_from_you=input()
        if(input_from_you.lower()=="done"):
            print("\nThis is the order you gave.\n")
            break
        else:
            try:
                id_of_item,quantity=map(int,input_from_you.split("-"))
                if(id_of_item<1 or id_of_item>2):
                    print("Enter the id given in the menu...")
                elif(quantity<1 or quantity>100):
                    print("Enter a valid quantity below 100.")
                else:
                    if(id_of_item not in orders):
                        orders[id_of_item]=quantity
                    else:
                        orders[id_of_item]=orders[id_of_item]+quantity
            except:
                print("Enter the text in the format\n\nID of the beverage - Quantity(number of items)\nMention one item each time.\nOr type 'done' if completed.")   
    if(len(orders)==0):
        print("You entered nothing.\nPlease provide the input...")
        calculatebev()
    else:
        time=datetime.now().hour
        if((time>=6 and time<12) or (time>=16 and time<=18)):
            items=hot_beverages()
        elif((time>=12 and time<16) or (time>18 and time <=22)):
            items=cold_beverages()
        print("ID  Name of beverage                            Price      Quantity      Total price  ")
        print("--------------------------------------------------------------------------------------")
        bev_bill=0
        for i in range(len(orders)):
            k=list(orders)[i]
            recipe=list(items)[k-1]
            bev_bill=bev_bill+(items[recipe]*orders[k])
            print(recipe.ljust(47," ")+str(items[recipe]).ljust(12," ")+str(orders[k]).ljust(15," ")+str(items[recipe]*orders[k]))
        print("---------------------------------------------------------------------------------------")
        print("Total bill                                                               Rs.",bev_bill,"\n\n")
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")
        total=total+bev_bill
        print("Total bill including food menu                                           Rs.",total,"\n")