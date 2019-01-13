import random
import ctypes
import os
import time
import winsound

ctypes.windll.kernel32.SetConsoleTitleW(f"Furnace Simulator 2019 - {time.ctime()}")

degree = 0
progress = 0

while True:

    print("Furnace Simulator 2019: help for some actions\nCase-insensitive: no\nRecommended: Do \"coal\" to increase the furnace temperature in order to start cooking food.\nCredits: do \"credits\" for credits.")
    name_for_progress = input("What is your name? This will be used for the stats command later: ")
    print("Proceed to cook now.\n")
    while True:
        place = input("Place something in the furnace: ")
        if place == "coal":
            if degree > 400:
                print("[!] Your furnace is too hot!")
            elif degree > 410:
                print("[!] You burnt your hand, ouch.")
            else:
                degree += 130
                print("You successfully put coal in the furnace. The temperature is now: {} degrees Celsius.".format(str(degree)))
        elif place == "cook":
            if int(degree) < 10:
                print("Guys, please stop, your furnace is about 0-10 degrees Celsius, that's cold, but even colder that you cannot cook anything.. Please.")
            elif degree > 400:
                print("[!] Your furnace is too hot! It's dangerous to touch the furnace if it's over 400 degrees Celsius.")
            elif degree > 410:
                print("[!] You burnt your hand, ouch.")
            else:
                responses1 = ["You cook some steak.", "You cook some beef and potatoes. Tasty.", "You cook a pizza, yay!", "You make some sandwich with eggs, that's tasty.",
                        "You cook some Russian borsch, cyka blyat.", "You cook some burgers, YAY!"]
                print(random.choice(responses1))
                progress += 1
        elif place == "temperature":
            if int(degree) > 400:
                print("Your temperature is too hot and thus cannot be shown. Do \"cool\" or \"cool it down\" to decrease the temperature.  Or: you can do \"temperature /r\" to see the temperatures if it's high.")
            else:
                print(f"The temperature of the furnace is " + str(degree) + " degrees Celsius.")
        elif place == "temperature /r":
            print(f"The temperature of the furnace is " + str(degree) + " degrees Celsius.")
        elif place == "help":
            print("""
stats - See the stats of your progress.
temperature - Check the furnace temperature.
temperature /r - Force show high temperatures.
cook - Cook some beef.
coal - Place some coal.
help - Some actions you can do.
fan - Fan the fire so you can make it hotter.
eat - Eat some food you cooked!
cool/cooldown - Decrease the furnace temperature.
clear - Clear the screen.
exit - Exit the simulator.
""")
        elif place == "fan":
            if int(degree) < 0:
                print("Oops! Your furnace is so cold, you don't need to fan it, it's cold.")
            else:
                print("You fan the fire 150 times. You succeeded.")
                progress += 1
                degree += 200
        elif place == "eat":
            responses2 = ["You eat some steak.", "You eat some beef and potatoes. Tasty.", "You eat a pizza, yay!", "You eat some sandwich with eggs, that's tasty.",
                            "You eat some Russian borsch.", "You eat some burgers."]
            print(random.choice(responses2))
            progress += 10
        elif place == "cool" or place == "cooldown":
            degree -= 105
            print(f"Your furnace temperature has been decreased by 105 degrees Celsius. The temperature of the furnace is: {str(degree)} degrees Celsius.")
            progress += 1
        elif place == "exit":
            quit()
        elif place == "clear":
            time.sleep(2)
            cls()
        elif degree > 410:
            print("[!] Your furnace is too hot! If you don't cool it down, it becomes dangerous to touch! Do \"cool\" or \"cooldown\" to cool it down.")
        elif place == "evaluate" or place == "eval" or place == "exec" or place == "execute":
            code = input("Eval mode: ")
            try:
                eval(code)
            except:
                print("Something went wrong. :(")
            finally:
                pass
        elif place == "stats":
            print(f"""
Player Name: {name_for_progress}
Game progress: {progress}%
Furnace temperature: {str(degree)}
""")
            if progress > 100:
                print(f"""
Player Name: {name_for_progress}
Game progress: 100% (This is the maximum!)
Furnace temperature: {str(degree)}
""")
        elif place == "credits":
            print("""
Developer: Windows 95#0001 (Henry Benson, this is a nickname not a real name) (Sam Gordon)
Language: Python
Multi-developers: None
--------------------------------------------------------
Written by a single developer
Original game written in Assembly and JS (but abandoned)
""")
        else:
            print("Oh noes! You burnt your hand when you tried to do an action that doesn't exist!")

def cls():
    os.system("cls")
