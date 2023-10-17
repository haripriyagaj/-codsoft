import random
def gaming():
    user_mark = 0
    comp_mark = 0
    print("Welcome to rock,paper and scissor game.")
    while True:
        user_choice = input("Enter your choice in rock,paper and scissor:")
        comp_choice = random.choice(["rock","paper","scissor"])
        print(f'You chose {user_choice}')
        print(f'computer chose {comp_choice}')
        if user_choice not in(["rock","paper","scissor"]):
            print("Invalid choice.Please try again. ")
        if user_choice == comp_choice:
            print("It's tie.please try again.")
            continue
        elif(user_choice=="rock"and comp_choice=="scissor")or(user_choice=="scissor"and comp_choice=="paper")or (user_choice=="paper"and comp_choice=="rock"):
            print("You won the game!")
            user_mark+=1
        else:
            print("Computer has won the game!")
            comp_mark+=1
        Player_choice = input("Do you want to play again?(yes/no)")
        if Player_choice!="yes":
            print(f'user_mark:{user_mark} or comp_mark:{comp_mark}')
            print("Thanks for playing!")
            break
gaming()

    

