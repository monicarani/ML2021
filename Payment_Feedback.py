"""
   This module returns the link for payment and asks for feedback.
"""

# Displays a link to pay the money, when the function is called...
def payment():
    print("You can pay the bill with the link given below.")
    print("\n------------------->Link<--------------------\n")
    print("Please type 'done' after the money transfer")
    while(True):
        process=input()
        if(process=="done"):
            print("Your payment is successful.\n\nThe food will be served with in few minutes.Hope you felt comfortable using me.\n")
            break
        else:
            print("Type done if completed...")
    print("Please provide a rating about me")

# Takes the feedback from the customer and thanks him, when the function is called...
def feedback():
    try:
        rating=int(input(("Type your response between  1 to 5 :   ")))
        if(rating<1 or rating>5 ):
            print("Please",end=" ")
            feedback()
        else:
            if(1<=rating<=3):
                print("Thanks for the feedback. I wish next time you would feel more comfortable.")
            else:
                print("Thanks for the feedback. Seems you have enjoyed using me.")
            print("\nHope you will have a great time here.")
            print("Visit again!!!")
    except:
        print("Enter valid text ...")
        feedback()


