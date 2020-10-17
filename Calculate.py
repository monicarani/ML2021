"""
   This module returns the bill of recipes.
"""
from datetime import datetime
from Menu import break_fast,lunch,snacks,dinner
def calculate():
    global total_bill
    orders={}
    while(True):
        input_from_you=input()
        if(input_from_you.lower()=="done"):
            print("\nThis is the order you gave.\n")
            break
        else:
            try:
                id_of_item,quantity=map(int,input_from_you.split("-"))
                if(id_of_item<1 or id_of_item>10):
                    print("Enter the id given in the menu...")
                elif(quantity<1 or quantity>100):
                    print("Enter a valid quantity below 100.")
                else:
                    if(id_of_item not in orders):
                        orders[id_of_item]=quantity
                    else:
                        orders[id_of_item]=orders[id_of_item]+quantity
            except:
                print("Enter the text in the format\n\nID of the recipe - Quantity(number of plates)\nMention one item each time.\nOr type 'done' if completed.")   
    if(len(orders)==0):
        print("You entered nothing.\nPlease provide the input...")
        calculate()
    else:
        time=datetime.now().hour
        if(time>=6 and time<12):
            items=break_fast()
        elif(time>=12 and time<16):
            items=lunch()
        elif(time>=16 and time<=18):
            items=snacks()
        elif(time>18 and time<=22):
            items=dinner()
        print("ID  Name of recipe                            Price      Quantity      Total price  ")
        print("--------------------------------------------------------------------------------------")
        total_bill=0
        for i in range(len(orders)):
            k=list(orders)[i]
            recipe=list(items)[k-1]
            total_bill=total_bill+(items[recipe]*orders[k])
            print(recipe.ljust(47," ")+str(items[recipe]).ljust(12," ")+str(orders[k]).ljust(15," ")+str(items[recipe]*orders[k]))
        print("---------------------------------------------------------------------------------------")
        print("Total bill                                                               Rs.",total_bill,"\n")

