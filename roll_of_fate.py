import pygame
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\semas\OneDrive\Documenten\roll_of_fate\assets\sound.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


import time

def slow_print(text, delay=0.06):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def check_tweespelers():
    while True:
        try:
            player_i = int(input("Enter how many players? "))
        except ValueError:
            continue

        if player_i == 1:
            print("The board whispers... no soul can face fate alone...")
            continue
        elif player_i >= 3:
            print("The path rejects the many… only two may walk together...")
            continue
        elif player_i == 2:
            print("Welcome, your fate is waiting for you....")
            break

def maak_twee_spelers():
    p1 = "Player 1"
    p2 = "Player 2"
    p1_score = 0
    p2_score = 0

    spelers = [p1, p2, p1_score, p2_score]
    return spelers

def points_for(choice):
    if choice == "help":
        return 2
    elif choice == "collect":
        return 1
    elif choice == "sabotage":
        return -2
    else:
        return 0

def ask_choice_for(player_label):
    choice = input(f"{player_label}  choose [help / collect / sabotage]: ").strip().lower()
    while choice not in ("help", "collect", "sabotage"):
        choice = input("Invalid. Choose [help / collect / sabotage]: ").strip().lower()
    return choice

def play_challenge(intro, spelers):
    # declaratie van een functie
    slow_print("\n--- A whisper stirs ---")
    slow_print(intro)

    c1 = ask_choice_for(spelers[0])
    spelers[2] += points_for(c1)
    time.sleep(0.4)

    c2 = ask_choice_for(spelers[1])
    spelers[3] += points_for(c2)
    time.sleep(0.4)

def uitvoeren_challenges(spelers):
# aanroepen (= uitvoeren) van een functie
    intro = "A voice whispers:\n'A soul is drowning in darkness... a hand reaches out. Will you take it?'"
    play_challenge(intro, spelers)

    play_challenge(
        "In the forest, glowing charms hum with power... but eyes are watching in the dark.'", spelers
    )

    play_challenge(
        "A deep voice murmurs:\n'The last gate demands sacrifice... Alone, you cannot pass.'", spelers
    )

def mirror_reflection(player_label, score):
    slow_print(f"\n--- The Mirror of Fate: {player_label} ---")
    slow_print("The mirror trembles before you... whispers of your past choices echo around...")
    time.sleep(0.7)
    slow_print("The reflection begins to speak...")
    time.sleep(0.7)

    if score >= 8:
        slow_print("The mirror blazes:\n'You carried the light. The path opens for you.'")
    elif score >= 4:
        slow_print("The mirror warms:\n'Flaws and courage—yet you moved forward.'")
    elif score >= 1:
        slow_print("The mirror hums:\n'Not lost… not found. Keep searching.'")
    elif score >= -3:
        slow_print("The mirror chills:\n'You reached for the light, but your shadow pulled you back.'")
    else:
        slow_print("The mirror darkens:\n'Shadow chose you… and you chose it back.'")

def score_doorgeven(p1, p2, p1_score, p2_score):
    mirror_reflection(p1, p1_score)
    mirror_reflection(p2, p2_score)

# The_Mind_Collapse!!
import time, sys, random

def mc_reverse(s: str) -> str:
    return s[::-1]

def mc_cold(text: str) -> str:
    return f"\033[36m{text}\033[0m"

def slow_print(text, delay=0.06):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

import os
# https://www.geeksforgeeks.org/python/clear-screen-python/
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mc_witch_end(spelers):
    p1, p2 = spelers[0], spelers[1]

    print()  

    lines = [
        "A voice rises from the mirror — it is your voice, but wrong. Older. Hungrier.",
        "\"I watched you long enough. Every choice, every fear… now they are mine.\"",
        "The witch smiles:",
        "\"I rest now. You continue my work.\""
    ]

    for line in lines:
        slow_print(line, 0.05)
        time.sleep(0.3)

    clear_screen()

    slow_print(">>> SYSTEM TRANSFER INITIATED <<<", 0.08)
    time.sleep(1.7)

    clear_screen()

    titles = ["Echo-One", "Echo-Two"]
    random.shuffle(titles)

    print(f"{mc_cold(p1)} → {titles[0]}")
    time.sleep(0.4)
    print(f"{mc_cold(p2)} → {titles[1]}")
    time.sleep(1.2)

def mc_false_awaken_end():
    slow_print("…system reloading psyche…", 0.07)
    time.sleep(2.5)

    slow_print("soul container locked.", 0.08)
    time.sleep(0.9)

    slow_print("Welcome back, captive soul.", 0.06)
    time.sleep(0.4)

    sys.exit(0)

def main():

    check_tweespelers()
    spelers = maak_twee_spelers()
    uitvoeren_challenges(spelers)
    score_doorgeven(spelers[0], spelers[1], spelers[2], spelers[3])
    slow_print("\nThe air shifts... something else awakens.", 0.06)
    mc_witch_end(spelers)
    mc_false_awaken_end()

