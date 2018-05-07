from time import sleep

def dead(why):
    print(why, "As expected.")

    for i in range(0, 5):
        print('.', end = ' ', flush = True)
        sleep(i/2)

    for i in range(0, 100):
        print("YOU ARE DEAD. GAME OVER. YOU ARE DEAD. GAME OVER. YOU ARE DEAD. GAME OVER. YOU ARE DEAD. GAME OVER.")
        sleep(0.01)

    exit(0)