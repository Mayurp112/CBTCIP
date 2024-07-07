import random

def generate_number(length):
    return ''.join(random.choices('0123456789', k=length))

def provide_feedback(secret, guess):
    correct_digits = sum(1 for s, g in zip(secret, guess) if s == g)
    correct_positions = len(set(secret) & set(guess)) - correct_digits
    return correct_digits, correct_positions

def play_game():
    length = int(input("Enter the length of the number to guess: "))
    

    player1_number = generate_number(length)
    print("Player 1 has set the number.")

    player1_attempts = 0
    player2_attempts = 0
    

    while True:
        player2_guess = input("Player 2, enter your guess: ")
        player2_attempts += 1
        correct_digits, correct_positions = provide_feedback(player1_number, player2_guess)
        if player2_guess == player1_number:
            print("Player 2 guessed the number")
            break
        else:
            print(f"Digits in the correct place: {correct_digits}")
            print(f"Correct digits but in the wrong place: {correct_positions}")

    
    print("\nSwitching roles...\n")
    
    player2_number = generate_number(length)
    print("Player 2 has set the number.")
    

    while True:
        player1_guess = input("Player 1, enter your guess: ")
        player1_attempts += 1
        correct_digits, correct_positions = provide_feedback(player2_number, player1_guess)
        if player1_guess == player2_number:
            print("Player 1 guessed the number")
            break
        else:
            print(f"Digits in the correct place: {correct_digits}")
            print(f"Correct digits but in the wrong place: {correct_positions}")


    print("\nGame Over")
    print(f"Player 1 attempts: {player1_attempts}")
    print(f"Player 2 attempts: {player2_attempts}")

    if player1_attempts < player2_attempts:
        print("Player 1 is the Mastermind")
    elif player2_attempts < player1_attempts:
        print("Player 2 is the Mastermind")
    else:
        print("It's a tie")

if __name__ == "__main__":
    play_game()
