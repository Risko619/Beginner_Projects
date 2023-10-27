print("Welcome to Risko's Quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play:-)")
score = 0

answer = input("What does CPU stand for? ").upper()
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

""" At this point I can copy and paste the above to create more Questions and Answers"""

answer = input(" What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
""" .lower makes the users input case-insensitive, so if they use capitals but the answer is right it will still be correct"""

print("You got " + str(score) + " questions correct!")
""" the above allows me to add an integar to a string"""
print("You got " + str((score / 4) * 100) + "%")
""" above line allows a percentage score """
   
