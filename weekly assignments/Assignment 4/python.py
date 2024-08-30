import random

def highlow_game():
    print("Welcome to the High-Low Game!")
    print("-----------------------------")
    rounds = 5
    score = 0
    for round_no in range(1, rounds +1):
        print(f"Round {round_no}")
        play_no = random.randint(1, 100)
        comp_no = random.randint(1, 100)
        print(f"Your number is {play_no}")
        guess = input("Do you think your number is higher or lower than the computer's? ").strip().lower()
        if (guess == "higher" and play_no > comp_no) or (guess == "lower" and play_no < comp_no):
         print(f"You were right! the computer's number was {comp_no}.")
         score +=1
        else:
            print(f"Nope! that's incorrect, the computer's number was {comp_no}.")
    
        print (f"Your score is now {score}\n")
    print("Thanks for playing!")

if __name__ == "__main__":
    highlow_game()