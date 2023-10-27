name = input("Type your name: ")
print("Welcome ", name, "to your Adventure, where your goal is to escape the misty woods")

answer = input("You have reached a dirt road. Do you want to go left or right? ").lower()

if answer == "left":
    answer = input("You came across a Lake. Do you swim across or walk around it? Type (w) for walk or (s) to swim ").lower()
    if answer == "s":
        print("You were eaten by a group of Aligators! You Lose.")
    elif answer == "w":
        print("As the night went on and walking several miles, you were eaten by a pack of wolves. You Lose.")
    else:
        print(name, "Please type 'w' or 's' to continue ")

elif answer == "right":
    answer = input("You come to a wobbly bridge. Do you want to cross it or head back? (Type 'cross' or 'back')")
    if answer == "back":
        print("You die by a giant troll lurking underneath. You Lose!")
    
    elif answer == "cross":
        answer = input("You cross the bridge safely and are met with a Wizard on the other end. Do you talk to him? (Type 'yes' or 'no')")
        if answer == "yes":
            print("The Wizard opens a portal that leads you out of the woods. You Win!")
        elif answer == "no":
            print("You ignore the Wizard and up falling into an Abyss. You Lose!")

else:
    print('Not a valid option. You lose.')

print("Thank you for playing", name)
        
    
