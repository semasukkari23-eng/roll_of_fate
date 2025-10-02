import pygame
pygame.mixer.init()
pygame.mixer.music.load("assets/sound.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    
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
        print("Welcome, your faith is waiting for you....")
        break
def run_game():
    score = 0
    challenges = [
        ("You wander into a dark forest and find a trapped spirit crying for help.", ("help","ignore","sabotage"), {"help":1,"ignore":-1,"sabotage":-2}),
        ("A glowing charm floats above the board, pulsing with energy.r", ("collect","leave","sabotage"), {"collect":1,"leave":-1,"sabotage":-2}),
        ("At the final gate of fate, a voice whispers: 'Will you aid your rival or hinder them?", ("help","forward","sabotage"), {"help":1,"forward":-1,"sabotage":-2})
    ]

    for name, opts, pts in challenges: 
        print(f"\n{name}:")
        print("Options:", ", ".join(opts))
        while True:
            choice = input("Choose action: ").strip().lower()
            if choice in opts:
                score += pts[choice]
                print("You chose:", choice)
                break
            print("Invalid — try again.")
    print("Final score:", score)

if __name__ == "__main__":
    run_game()


