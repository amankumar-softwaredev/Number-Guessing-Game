from random import randint

number_random = randint(20, 30)

while True:
    try:
        number_guess = int(input("ENTER YOUR NUMBER TO GUESS (BETWEEN 20 AND 30): "))

    except Exception:
        print("PLEASE ENTER A VALID INTEGER NUMBER.")
        break

    if(number_guess > number_random or number_guess < number_random):
        print("PLEASE ENTER A NUMBER BETWEEN 20 AND 30 (INCLUDING BOTH).")

    if(number_guess == number_random):
        print(f"CORRECT! THE NUMBER WAS: {number_random}")
        print("YOU ARE THE WINNER!")
        break

    else:
        print("YOU ARE NOT WINNER! ")


