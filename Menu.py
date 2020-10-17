"""
   This module returns the menu items.
"""
from datetime import datetime
time=datetime.now().hour
def break_fast():
    breakfast_items={"1.  Aloo Paratha ":30,"2.  Semiya Upma ":35,"3.  Masala Dosa ":25,"4.  Poori ":20,"5.  Idli(Sambar) ":20,"6.  Vada ":15,"7.  Ragi Rava Upma ":30,"8.  Rava Utappam ":35,"9.  Bread Omelette ":30,"10. Green Salad ":30}
    return breakfast_items
def lunch():
    lunch_items={"1.  Veg Thali ":50,"2.  Veg Biryani ":45,"3.  Lemon Rice ":30,"4.  Tomato Rice ":30,"5.  Mushroom Biryani ":40,"6.  Naan-Butter Paneer Masala ":40,"7.  Non-Veg Thali ":60,"8.  One-pot Chicken Biryani ":65,"9.  Prawn Biryani ":70,"10. Curd Rice ":30}
    return lunch_items
def snacks():
    snack_items={"1.  Pav Bhaji ":30,"2.  Paneer Tikka ":30,"3.  Spring Rolls ":20,"4.  Gobi Manchurian ":30,"5.  Veg grilled Sandwich ":25,"6.  Chilli Babycorn ":25,"7.  Paneer naan Pizza ":35,"8.  Egg Pakora ":35,"9.  Fire Chicken ":40,"10. Fish 65 ":50}
    return snack_items
def dinner():
    dinner_items={"1.  Tomato Soup ":30,"2.  Veg corn Soup ":30,"3.  Soya Salad ":35,"4.  Pulka-mixed vegetable curry ":40,"5.  Veg Thali ":50,"6.  Vegetable Pulao ":45,"7.  Chicken Fried rice ":55,"8.  Non-veg Thali ":60,"9.  One-pot Mushroom Biryani ":50,"10. Curd rice ":30}
    return dinner_items
def hot_beverages():
    hotbeverages={"1.  Tea ":10,"2.  Coffee ":8}
    return hotbeverages
def cold_beverages():
    coldbeverages={"1.  Thumpsup ":15,"2.  Sprite ":15}
    return coldbeverages

def menu():
    if(time>=6 and time<12):
        items=break_fast()
    if(time>=12 and time<16):
        items=lunch()
    elif(time>=16 and time<=18):
        items=snacks()
    elif(time>18 and time<=22):
        items=dinner()
    print("\nID  Name of recipe                             Price")
    print("------------------------------------------------------")
    for i in items:
        print(i.ljust(45," "),"Rs.",items[i])
    print()
def beverages():
    if((time>=6 and time<12) or (time>=16 and time<=18)):
        drinks=hot_beverages()
    elif((time>=12 and time<16) or (time>18 and time <=22)):
        drinks=cold_beverages()
    print("\nID  Name of beverage                             Price")
    print("------------------------------------------------------")
    for i in drinks:
        print(i.ljust(45," "),"Rs.",drinks[i])
    print()


