print("Welcome to my quiz game!!!")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()

print("Let's go!")
score = 0 

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

if score == 1:
    print("You got " + str(score) + " question correct which equal to " 
          + str((1/4)*100) + "%.")
      
else: 
    print("You got " + str(score) + " questions correct which equal to " 
          + str((score/4)*100) + "%.")


