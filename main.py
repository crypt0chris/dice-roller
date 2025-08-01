#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time

def roll_dice():
    dice_faces = {
        1: (
            "+-----+\n"
            "|     |\n"
            "|  o  |\n"
            "|     |\n"
            "+-----+"
        ),
        2: (
            "+-----+\n"
            "| o   |\n"
            "|     |\n"
            "|   o |\n"
            "+-----+"
        ),
        3: (
            "+-----+\n"
            "| o   |\n"
            "|  o  |\n"
            "|   o |\n"
            "+-----+"
        ),
        4: (
            "+-----+\n"
            "| o o |\n"
            "|     |\n"
            "| o o |\n"
            "+-----+"
        ),
        5: (
            "+-----+\n"
            "| o o |\n"
            "|  o  |\n"
            "| o o |\n"
            "+-----+"
        ),
        6: (
            "+-----+\n"
            "| o o |\n"
            "| o o |\n"
            "| o o |\n"
            "+-----+"
        )
    }

    def animate_roll(dice_faces, result):
        print("\n🎲 Rolling the dice...\n", flush=True)
        for _ in range(15):  # Longer animation
            face = random.choice(list(dice_faces.values()))
            print("\033c", end="")  # Clear screen
            print(f"{face}\n", flush=True)
            time.sleep(0.1)
        final_face = dice_faces[result]
        print("\033c", end="")  # Clear screen
        print(f"{final_face}\n")

    while True:
        input("🎲 Hit Enter to roll the dice...")
        roll = random.randint(1, 6)
        animate_roll(dice_faces, roll)
        print(f"🎯 You rolled a {roll}!")
        again = input("🔁 Roll again? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    try:
        roll_dice()
    except KeyboardInterrupt:
        print("\n👋 Exiting dice roller. Goodbye!\n")
