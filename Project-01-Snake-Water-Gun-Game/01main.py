import random
user = input("enter s for snake, w for water and g for gun: ")
computer = random.choice(['s', 'w', 'g'])
print(f'you chose: {user} | computer chose: {computer}')


if user==computer:
    print("draw")
else:
    if user=="s" and computer=="w":
        print('you win')
    elif user=="w" and computer=="g":
        print("you win")
    elif user=="g" and computer=="s":
        print("you won")
    else:
        print("computer wins")




# another way to solve the same problem:
def get_user_choice():
    user = input("Enter s, w, or g: ")
    return user

def get_comp_choice():
    computer = random.choice(['s', 'w', 'g'])
    return computer

def find_winner(user, computer):
    if(user == computer):
        return "draw"
    elif user == "s" and computer == "w":
        return 'you win'
    elif user == 'w' and computer == 'g':
        return 'you win'
    elif user == 'g' and computer == 's':
        return 'you win'
    else:
        return 'computer wins'

# this line also works the same but we have to but we have to remove the line below this line
# print(find_winner(get_user_choice(), get_comp_choice()))
user = get_user_choice()
print("user chose", user)
computer = get_comp_choice()
print("computer chose", computer)
print(f'winner is {find_winner(user, computer)} : {computer}')



# another way to solve the same problem using dict.
def user_input():
    user = input("Enter the choices s, w, g: ")
    return user

def comp_input():
    computer = random.choice(['s', 'w', 'g'])
    return computer

def refree_to_decide_winner(user, computer):
    if(user == computer):
        return "draw"
    elif user == "s" and computer == "w":
        return 'you win'
    elif user == 'w' and computer == 'g':
        return 'you win'
    elif user == 'g' and computer == 's':
        return 'you win'
    else:
        return 'computer wins'

user = user_input()
computer = comp_input()
choices = {
    's' : 'snake',
    'w' : 'water',
    'g' : 'gun'
}

print('user chose', choices[user])
print('computer chose', choices[computer])
print('winner is:', refree_to_decide_winner(user, computer))



# write me the program when user enter other characters instead of s, w, g suppose he enters h I want to return valid use s, w, g
def user_input():
    user = input("Enter your choice (s, w, g): ")
    if user == "s" or user == "w" or user == "g":
        return user
    else:
        return "Invalid"

def comp_input():
    return random.choice(['s', 'w', 'g'])

def referee_to_decide_winner(user, computer):
    if user == computer:
        return "Draw"
    elif user == "s" and computer == "w":
        return "You Win"
    elif user == "w" and computer == "g":
        return "You Win"
    elif user == "g" and computer == "s":
        return "You Win"
    else:
        return "Computer Wins"

choices = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}
user = user_input()
if user == "Invalid":
    print("Invalid Choice! Please enter only s, w, or g to play the game")
else:
    computer = comp_input()

    print("User chose:", choices[user])
    print("Computer chose:", choices[computer])
    print("Winner:", referee_to_decide_winner(user, computer))