def play_game():
    """
    Simulate the initial scenario and prompt the player to make a choice.

    Returns:
        str: The player's choice.
    """
    print("You stare out across a vast space of black. There is no sound, there is no people, there is nothing.")
    print("1. [Call out]")
    print("2. [Stand there in silence]")
    print("3. [Attempt to get out of the void]")
    pick = input("How would you like to respond?: ")
    if pick == '1':
        print("As you stand in the void, your voice echoes faintly, dissipating into the empty expanse. The silence weighs heavy, almost tangible. You try to discern any signs of life or direction but find nothing. It's as if you're suspended in an abyss, disconnected from everything familiar.")
        return '1'  
    elif pick == '2':
        print("...")
        return '3'  # Return '3' for scenario 2
    elif pick == '3':
        print("You start running faster in faster into the dark abyss, but it feels like you’re running through mud. Even if you were making progress getting out of this void, you’d have nothing to show for it.")
        return '1'and'2'  # Return '2' for both scenarios 1 and 3
    print("{Suddenly, a square pops up in the void.}")

def round_1():
    pick = play_game()
    print(f"1. [Attack the square]")
    print(f"2. [Stare at the square]")
    print(f"3. [Hug the square]")
    print(f"4. [Run away from the square]")
    pick = input("How would you like to respond?: ")
    if pick == '1':
        print("When you swing your fist toward the square it starts glowing an angry red. \n Mysterious Square: 'I beg your finest pardon! Treat me with some respect mortal!'")
        return '2' and '4'
    elif pick == '2':
        print("The square seems to be observing you as well. A small hum of power is emanating from the geometric shape as it turns a shade of purple.")
        return '1' and '3'
    elif pick == '3':
        print("The square seems to hum with power as you embrace the shape. Its body starts to turn a light shade of pink.")
        return '1' and '3'
    elif pick == '4':
        print("Goosebumps rise on the back of your neck as the square seems to loom over you. As you run away from the mysterious object it seems to follow you gliding easily in the void as you struggle to get away.")
        return '2'
    print("Mysterious Square: I am the God of your world. You have reached the end of your previous life and now it's time to place you in another world.")

def round_2():
    pick = play_game()
    print(f"1. [Question how you died in your previous life]")
    print(f"2. [Thank the square for granting you a new lease on life]")
    print(f"3. [Defy the square]")
    pick = input("How would you like to respond?: ")
    if pick == '1':
        print("Mysterious Square: While crossing the street, a delivery truck crashed into you.")
        print(f"1. [Acceptance/Resignation]")
        print(f"2. [Anger]")
        print(f"3. [Regret/Bargaining]")
        print(f"4. [Shock]")
        pick = input("How would you like to respond?: ")
        if pick == '1':
            print("Mysterious Square: You adjust quite quickly don't you?")
            return '1' and '3'
        elif pick == '2':
            print("Mysterious Square: A reasonable response to your untimely end.")
            return '1' and '2'
        elif pick == '3':
            print("Mysterious Square: There's nothing you can do now. Your body is no longer available to host your soul.")
            return '2' and '4'
        elif pick == '4':
            print("Mysterious Square: A reasonable response to your untimely end.")
            return '3'
        return '4'
    elif pick == '2':
        print("Mysterious Square: Well, it was kind of my fault that your life was cut to an end so soon. The square pauses before continuing on...")
        return '3'
    elif pick == '3':
        print("Mysterious Square: Such insolence for a being that’s about to send you to another world.")
        print(f"1. [Apologize]")
        print(f"2. [Remain Defiant]")
        print(f"3. [Stay Silent]")
        pick = input("How would you like to respond?: ")

        if pick == '1':
            return '1' and '3'
        elif pick == '2':
            return '2' and '4'
        elif pick == '3':
            return '4'
        return '1' and '2'
    print ("Mysterious Square: Now, you must answer these three questions before I send you down to live your next life.")

def round_3():
    pick = play_game()
    print ("Mysterious Square: Who did you love most in life?")
    print(f"1. [Family]")
    print(f"2. [Friends]")
    print(f"3. [Significant Other]")
    print(f"4. [Yourself]")
    pick = input("How would you like to respond?: ")
    if pick == '1':
        return '1' and '3'
    elif pick == '2':
        return '3'
    elif pick == '3':
        return '1' and '2'
    elif print == '4':
        return '1' and '4'

def round_4():
    pick = play_game()
    print("Mysterious Square: How do you think you made an impact on the world?")
    print(f"1. [Relationships]")
    print(f"2. [Social/Environmental Works]")
    print(f"3. [Creativite Works]")
    print(f"4. [Nothing]")
    pick = input("How would you like to respond?: ")
    if pick == '1':
        return '1' and '3'
    elif pick == '2':
        return '1' and '2'
    elif pick == '3':
        return '2' and '3'
    elif print == '4':
        return '4'    

def round_5():
    pick = play_game()
    print("Mysterious Square: When would you have wanted to go?")
    print(f"1. [Sooner]")
    print(f"2. [Later]")
    print(f"3. [Now]")
    print(f"4. [Never]")
    pick = input("How would you like to respond?: ")
    if pick == '1':
        return '2' and '3'
    elif pick == '2':
        return '1' and '3'
    elif pick == '3':
        return '2' and '1'
    elif print == '4':
        return '4'  
    print("Mysterious Square: Thank you for answering my questions. Off you go to your next life then.")

def main():
    ending_counts = {'1': 0, '2': 0, '3': 0, '4': 0}

    result = round_1()
    ending_counts[result] += 1

    result = round_2()
    ending_counts[result] += 1

    majority_ending = max(ending_counts, key=ending_counts.get)    
    if majority_ending == '1':
        print("ENDING 1: PROTAGONIST")
    elif majority_ending == '2':
        print("ENDING 2: VILLAIN")
    elif majority_ending == '3':
        print("ENDING 3: SIDE CHARACTER")
    else:
        print("SECRET ENDING: GOD")

if __name__ == "__main__":
    main()
