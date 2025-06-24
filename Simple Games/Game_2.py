import random

print("This is a rock, paper scissors game.")
print("Defeat the computer to win!")
print("-------------------------------")

#choice to play
choice = str(input("Do you want to play?")).lower()
if choice == "yes":
    name = input("What is your name?")
    print("Hello", name, "let us begin!")
elif choice == "no":
    print("Alright! Come back when you want to play")
    exit()

#choice for defeating the comp
def play():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return print("It's a tie, sorry", name) #function

    # R > S, S > P, P > R
    if is_win(user, computer):
        return print("You won!",name)

    return print("You lost!",name)

def is_win(player, opponent):
    # return true if player wins
    # R > S, S > P, P > R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
        or (player == 'P' and opponent == 'R'):
        return True

print(play())