while True:
    # asking the user to enter his name

    name = input("enter name: ")

    # welcoming the user to the andventure

    print("welcome", name, "to this adventure\n from where would you like to start?")

    # start

    print("you've been travelling and u've reached a dead end\n you can either go right or left")
    start = input("where do you wanna go? (left/right)").lower()
    if start != "right" and start != "left":
        print("thats not a valid option please re-enter where do you want to go:")
        continue
