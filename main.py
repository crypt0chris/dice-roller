import random

def roll_dice():
    while True:
        input("Press Enter to roll the dice...")
        print("You rolled a", random.randint(1, 6))
        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    roll_dice()
