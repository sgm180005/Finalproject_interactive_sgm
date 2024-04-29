def choices(question):
    print("\n" + question)
    choice = input("Enter Your Choice [1/2/3/4]: ")
    while(True):
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Enter again")
            choice = input("Enter Choice [1/2/3/4]: ")

def play_round(pick):
    # TODO: Implement code & docstring
    if pick == "1":
            return 1
    elif pick == "2":
            return 2
    elif pick == "3":
            return 3 
    else:
         return 4    

def play_game():
    # TODO: Implement code & docstring
   
    print("You stare out across a vast space of black. There is no sound, there is no people, there is nothing.")
    print(f"1. [Call out]")
    print(f"2. [Stand there in silence]")
    print(f"3. [Attempt to get out of the void]")
    pick = input("How would you like to respond?: ")
    print("{Suddenly, a square pops up in the void.}")
    round1 = play_round(pick)
    print(f"1. [Attack the square]")
    print(f"2. [Stare at the square]")
    print(f"3. [Hug the square]")
    print(f"4. [Run away from the square]")
    pick = input("How would you like to respond?: ")
    print("I am the God of your world. You have reached the end of your previous life and now it's time to place you in another world.")
    round2 = play_round(pick)
    print(f"1. [Question the square]")
    print(f"2. [Thank the square]")
    print(f"3. [Defy the square]")
    pick = input("How would you like to respond?: ")
    round3 = play_round(pick)
    p1_score = (round1 == 1) + (round2 == 1) + (round3 == 1)
    p2_score = (round1 == 2) + (round2 == 2) + (round3 == 2)
    
    if p1_score > p2_score:
        return 1
    elif p1_score < p2_score:
        return 2
    else:
        return 0

def main():
    result = play_game()
    if result == 1:
        print(f"Ending 1")
    elif result == 2:
         print(f"Ending 2")
    elif result == 3:
        print(f"Ending 3")
    else:
         print(f"Ending 4")

if __name__ == "__main__":
    main()