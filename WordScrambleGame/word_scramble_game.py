import random

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def play_game():
    words = ["apple", "python", "school", "library", "banana", "planet", "laptop", "mouse", "jumble", "coffee"]
    original_word = random.choice(words)
    scrambled = scramble_word(original_word)

    print("\nWelcome to the Word Scramble Game!")
    print("Guess the word from the scrambled letters.")
    print(f"\nScrambled word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input("Enter your guess: ").strip().lower()
        if guess == original_word:
            print(" Congratulations! You've guessed the correct word!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f" Wrong guess! You have {attempts} attempt(s) left.")
            else:
                print(f" Out of attempts! The correct word was: {original_word}")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print(" Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
