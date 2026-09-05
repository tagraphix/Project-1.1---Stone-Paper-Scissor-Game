# Stone, Paper, Scissor Game
'''
1 for Stone
-1 for Paper
0 for Scissor
'''


import pyttsx3 #text to speech module
import random #random module

#defining function for pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

user_score = 0
computer_score = 0
for i in range(5):

    print("Stone, Paper, Scissor")
    speak("Stone, Paper, Scissor. Please Enter your choice:")


    computer = random.choice([-1, 0, 1]) #random.choice for choosing randomly
    youstr = input("Enter your choice: ")
    youDict =  {"s":1, "p":-1, "sc":0}
    reversedDict = {1:"Stone", -1: "Paper", 0:"Scissor"}

    #add the input of user (i.e. youstr) in dictionary (i.e.youDict) and assign the value to you
    you = youDict[youstr]

    #By now we have 2 numbers (variables), you and computer

    print(f"You chose {reversedDict[you]} \nComputer chose {reversedDict[computer]}")
    speak(f"You chose {reversedDict[you]} \nComputer chose {reversedDict[computer]}")

    if(computer == you):
        print("It's a draw!")
        speak("It's a draw!")

    else: 
        if(computer == 1 and you == -1):
            print("You Win!")
            speak("You Win!")
            user_score += 1

        elif(computer == 1 and you == 0):
            print("You Lose!")
            speak("You Lose!")
            computer_score += 1

        elif(computer == -1 and you == 1):
            print("You Lose!")
            speak("You Lose!")
            computer_score += 1
            

        elif(computer == -1 and you == 0):
            print("You Win!")
            speak("You Win!")
            user_score += 1

        elif(computer == 0 and you == 1):
            print("You Win!")
            speak("You Win!")
            user_score += 1

        elif(computer == 0 and you == -1):
            print("You Lose!")
            speak("You Lose!")
            computer_score += 1

        else:
            print("Something went wrong!")



print("\n===== Final Score =====")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game!")
    speak("Congratulations! You won the game!")

elif computer_score > user_score:
    print("Computer won the game!")
    speak("Computer won the game!")

else:
    print("The game is a draw!")
    speak("The game is a draw!")