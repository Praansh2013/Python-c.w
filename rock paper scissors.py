import random
while True:
    actions=["Rock","Paper","Scissors"]
    user_choice=str(input("Enter your choice(Rock,Paper,Scissors): "))
    program_choice=random.choice(actions)
    print(f"Your choice is {user_choice}, computer's choice is {program_choice}\n")

    if user_choice==program_choice:
        print(f"Both players selected {user_choice}. It is a tie!")
    elif user_choice=="Rock":
        if program_choice=="Scissors":
            print("You won! as Rock smashes Scissors.")
        else:
            print("You loose :( as Paper covers Rock!")
    elif user_choice=="Paper":
        if program_choice=="Rock":
         print("You won! as Paper covers Rock.")
        else:
            print("You loose :( as Scissors cuts Paper!")
    elif user_choice=="Scissors":
        if program_choice=="Paper":
            print("You won! as Scissors cuts Paper.")
        else:
            print("You lose :( as Rock smashes Scissors.")
    play_again=str(input("Play agin? (y/n): "))
    if play_again.lower()!="y":
        break