"""
First Period Frenzy
You have to get to class before the bell rings!
Your choices affect your time and your chances of success.
"""

state = "waking_up"
time_left = 10
energy = 3

print("Your alarm goes off! You have 10 minutes to get to first period.")

while state not in ("in_class", "late"):
    print(f"\n[STATE: {state.upper()} | Time left: {time_left} min | Energy: {energy}]")

    if state == "waking_up":
        choice = input("Do you (g)et up immediately or (s)nooze? ").lower()

        if choice == "g":
            print("You jump out of bed and get ready!")
            time_left -= 2
            state = "getting_ready"
        elif choice == "s":
            print("You snooze and almost fall back asleep!")
            time_left -= 5
            energy += 1
            state = "getting_ready"
        else:
            print("Choose g or s.")

    elif state == "getting_ready":
        choice = input("Do you (e)at breakfast or (s)kip it? ").lower()

        if choice == "e":
            print("You eat quickly and feel more energized.")
            energy += 1
            time_left -= 3
        elif choice == "s":
            print("You skip breakfast and rush out.")
            time_left -= 1
        else:
            print("Choose e or s.")

        if time_left <= 0:
            state = "late"
        else:
            state = "traveling"

    elif state == "traveling":
        choice = input("Do you (r)un to school or (w)alk normally? ").lower()

        if choice == "r":
            print("You run as fast as you can!")
            time_left -= 3
            energy -= 1
        elif choice == "w":
            print("You walk at a normal pace.")
            time_left -= 5
        else:
            print("Choose r or w.")
            continue

        if time_left <= 0:
            state = "late"
        elif energy >= 3:
            print("Your energy helps you get to school in time!")
            state = "in_class"
        else:
            print("You are exhausted and have to hurry the rest of the way.")
            state = "last_dash"

    elif state == "last_dash":
        choice = input("The bell is about to ring! Do you (s)print or (w)alk? ").lower()

        if choice == "s":
            print("You make one final sprint into class!")
            time_left -= 1
            if time_left > 0:
                state = "in_class"
            else:
                state = "late"
        elif choice == "w":
            print("You walk slowly and arrive after the bell.")
            state = "late"
        else:
            print("Choose s or w.")

print(f"\n[STATE: {state.upper()} | Time left: {time_left} | Energy: {energy}]")

if state == "in_class":
    print("You made it to first period on time! Your teacher gives you a nod.")
else:
    print("You arrived late. Your teacher asks why you weren't on time.")
