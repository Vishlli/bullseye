            # ||       || |||||| ||     ||||||  |||||   |||   |||  ||||||       ||||||||  |||||
            # ||       || ||     ||     ||     ||   || || || || || ||              ||    ||   ||
            # ||  |||  || |||||| ||     ||     ||   || ||  |||  || ||||||          ||    ||   ||
            # || || || || ||     ||     ||     ||   || ||       || ||              ||    ||   ||
            #  |||   |||  |||||| |||||| ||||||  |||||  ||       || ||||||          ||     |||||

                        # |||||  ||   || ||     ||     |||||| ||||||| ||  || ||||||
                        # ||  || ||   || ||     ||     |||    ||      ||  || ||
                        # |||||  ||   || ||     ||     |||||| |||||||  ||||  ||||||
                        # ||  || ||   || ||     ||        ||| ||        ||   ||
                        # |||||   |||||  |||||| |||||| |||||| |||||||   ||   ||||||

                                                                           ######
                                                                          #      #
                                                                          #  $$  #
                                                                          #      #
                                                                           ######
#                                                                            ||
# __________________________________________________________________________//\\_________________________________


import random
import tkinter as tk
from tkinter import messagebox

def show_instructions():
    root = tk.Tk()
    root.withdraw()



    messagebox.showinfo(
        "WELCOME TO BULLSEYE GUESSING GAME!",
        "How to Play:\n\n"
        "1. Enter a level to set the range for guessing. This must be a valid positive integer.\n"
        "2. Start guessing the number. ASCII art will guide you.\n"
        "3. '|' indicates the arrow. This is basically like a number-line.\n"
        "     * The arrow indicates how close your number is to the bullseye\n"
        "4. Visual hints shows how close you are:\n"
        "   - Big distance:   Far away!\n"
        "   - Big distance but CLOSER to target by a range of 7:\n Aim closer, almost there\n"
        "   - Smaller distance but CLOSER to target by a range of 7:\n Aim farther!, almost there\n"
        "   - Small distance:\n Almost there!\n"
        "   - Out of range:\n Guess is out of range\n"
        "   - Exact match:\n Bullseye!\n\n"
        
        "Scoring System:\n"
        "Your score starts at 100 points. Each incorrect guess deducts 5 points from your total.\n"
        "For example, if you make 3 incorrect guesses, 15 points will be deducted from 100, "
        "giving you a final score of 85 points.\n\n"
        "The fewer guesses you take to hit the bullseye, the higher your score! Aim carefully!\n\n"
        "Enjoy and good luck hitting the bullseye!"
    )
    root.quit()


def positive(p):
    while True:
        try:
            some = int(input(p))
            if some > 0:
                return some
            else:
                print("Please enter a positive number: ")
        except ValueError:
            pass

def main():
    print("""     
                  ||       || |||||| ||     ||||||  |||||   |||   |||  ||||||       ||||||||  |||||
                  ||       || ||     ||     ||     ||   || || || || || ||              ||    ||   ||
                  ||  |||  || |||||| ||     ||     ||   || ||  |||  || ||||||          ||    ||   ||
                  || || || || ||     ||     ||     ||   || ||       || ||              ||    ||   ||
                   |||   |||  |||||| |||||| ||||||  |||||  ||       || ||||||          ||     |||||

                             |||||  ||   || ||     ||     |||||| ||||||| ||  || ||||||
                             ||  || ||   || ||     ||     |||    ||      ||  || ||
                             |||||  ||   || ||     ||     |||||| |||||||  ||||  ||||||
                             ||  || ||   || ||     ||        ||| ||        ||   ||
                             |||||   |||||  |||||| |||||| |||||| |||||||   ||   ||||||

                                                                           ######
                                                                          #      #
                                                                          # ^ ^  #
                                                                          #  V   #
                                                                           ######
                                                                             ||
    ________________________________________________________________________///\_____________________________________
        """)
    num = positive("Please enter the level: ")
    com = random.randint(1, num)
    total = 100
    guesses = 0

    while True:
        guess = positive("Guess: ")
        guesses += 1

        if guess > num:
            print("""                                                       ######
                                                      #      #
                                                      # - -  #
                                                      #  -   #
                                                       ######
                                                         ||                               
            ____________________________________________///\____________________________________________
            """)
            print("                                                 Out of the field -_-\n")
        elif guess != com:
            if guess > com and (guess - com) >= 7:
                print("""                                                        ######
                                                       #      #
                                                       # -  - #
                                                       #  /\  #
                                                        ######
                                                          ||                               |
                _________________________________________///\_____________________________ * _____________
                """)
                print("                                                   Away! Aim closer\n")
            elif guess > com and (guess - com) < 7:
                print("""                                                        ######
                                                       #      #
                                                       # x x  #
                                                       #  =   #
                                                        ######
                                                          ||                  |
                _________________________________________///\________________ * __________________________
                """)
                print("                                               Aim closer, almost there\n")
            elif guess < com and (com - guess) < 7:
                print("""                                                        ######
                                                       #      #
                                                       # 6 6  #
                                                       #  o   #
                                                        ######
                                       |                  ||                              
                ______________________ * ________________///\______________________________________________
                """)
                print("                                               Aim farther!, almost there\n")
            else:
                print("""                                                        ######
                                                       #      #
                                                       # 0 0  #
                                                       #  -   #
                                                        ######
                          |                               ||                               
                _________ * _____________________________///\____________________________________________
                """)
                print("                                                     Aim farther!\n")
        else:
            print("""                                                        ######
                                                       #      #
                                                       # * *  #
                                                       # \_/  #
                                                        ######
                                                          ||
            _____________________________________________///\____________________________________________
            """)
            print("                                                You've hit the BULLSEYE!\n")
            break

    score = max(0, (total - (guesses - 1) * 5))
    print("                                                       Game Over")
    print(f"                                                 Your score is: {score}/100")
    print(f"                                         You took {guesses} guesses to hit the bullseye\n")
    play = input("Do you want to play again?(Y/N): ").upper()

    if play == "Y":
        main()

if __name__=="__main__":
    show_instructions()
    main()