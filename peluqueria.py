hours = 24
while hours < 0 or hours > 23:
    hours = int(input("Input a numbers between 0 and 23: "))
    if 6 <= hours <= 11:
        print(f"it is {hours}:00 it is morning")
    elif 12 <= hours <= 17:
        print(f"its is {hours}:00 it is afternoon")
    elif 18 <= hours <= 22:
        print(f"it is{hours}:00 it is night")
    else:
        print(f"it is {hours}:00 you are outside allowed hours")
