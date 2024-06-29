import random

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissor']

while True:
    user_input = input("Please enter rock/paper/scissor or q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick =  options[random_number]
    print("computer picks " + computer_pick + ".")

    if(user_input == 'rock' and computer_pick == 'paper'):
        print("computer wins.")
        computer_wins += 1

    elif(user_input == 'paper' and computer_pick == 'scissor'):
        print("computer wins.")
        computer_wins += 1

    elif(user_input == 'scissor' and computer_pick == 'rock'):
        print("computer wins")
        computer_wins += 1
    
    elif (user_input == computer_pick):
        print("draw")

    else:
        print("congrats!!! you won.")
        user_wins += 1

print("you won ", user_wins, " times")
print("computer won", user_wins, "times")
print("computer wins overall") if(computer_wins>user_wins) else print("you win the challenge")
