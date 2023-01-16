import time
import random
choose = ["rock", "paper", "scissors"]
mad_person_option = random.choice(choose)
name = input("enter name: ")
print("tm8: i finally found you", name, "cmon hop in, i got the weapons we need in the car trunk")
time.sleep(1)
print()

time.sleep(1)

print("tm8: Ah shit, we've reached a dead end i guess we gotta go on foot\nwe can either go right or left, whats your choice?", name)
print()
print("(right/left)")
r_l = input().replace(" ", "").lower()
if r_l == "right":
    print("tm8: we reached a forest, there are bananas lets pick them for later,")
    ban = input("pick/leave").replace(" ", "").lower()
    if ban == "pick":
        print("you died because the monkeys of the forest got mad and beat you up")
    if ban == "leave":
        print("tm8: bruh u r annoying we could've eaten those bananas, anyways lets move on!")
        time.sleep(3)
        print("tm8: oh we reached a forest full of apple trees, im gonna pick them and not gonna listen to you")
        time.sleep(5)
        print("* two minutes later  *")
        time.sleep(3)
        print("tm8 died of the apples because they were from the forest of the snow white one")
        one80 = input("Q to quit and C to continue alone").lower().replace(" ", "")
        if one80 == "q":
            quit()
        if one80 == "c":
            print("you bury your friend in the ground and find some gold in that spot")
            time.sleep(2)
            print("you keep moving on till you find a main road")
            time.sleep(2)
            print("* you wave to a car coming by *")
            time.sleep(1)
            print("you ask for a delivery and you thought you won")
            print()
            print("but instead they rob you and put you under unconsciousness and steal your money ")
            time.sleep(1)
            print("after you wake up")
            print("you realise you're lost and lost your money and family and your friends")
            time.sleep(1)
            print("congratulations, you played yourself, you died of depression")
if r_l == "left":
    print("tm8: ah man not a swamp and not the back got closed of trees\noh i found an entrance to somewhere\n do you wanna cross the swamp or go to the new entrance?\n")
    r_e = input("right or cross").replace(" ", "").lower()
    if r_e == "cross":
        print("You lost the game cause of crocodiles hiding in the swamp")
        quit()
    if r_e == "right":
        print("someone crazy: oh hi there")
        tt = input("ignore/talk").replace(" ", "").lower()
        if tt == "ignore":
            print("you lost the game cause of the person you met was mad crazy, got offended and then shot you ")
            quit()
        if tt == "talk":
            print("the mad crazy person: letS play togetHer rOck paper scissOrs maTe,\nif you win you get to shoot ME if not i shoot you\n(read cap letters together)")
            person_choose = input("think carefully: ").replace(" ", "").lower()


            if person_choose == mad_person_option:
                print("you lost the game to the rules of the mad person (tie) he picked", mad_person_option)
                quit()
            if person_choose == "rock" and mad_person_option == "paper" or person_choose == "paper" and mad_person_option == "scissors" or person_choose == "scissors" and mad_person_option == "rock":
                print("you died because he shot you, mad persons pick:", mad_person_option )
            if person_choose == "rock" and mad_person_option == "scissors" or person_choose == "paper" and mad_person_option == "rock" or person_choose == "scissors" and mad_person_option == "paper" or person_choose == "shoot" and mad_person_option == mad_person_option:
                print("tm8: man you had some courage jeez, thanks u saved us")
                print()
                time.sleep(2)
                print("tm8: ok lets keep going forward until we exit this god damn place\nIm gonna be fucked up if i see one more madass person lol")
                time.sleep(2)
                print()
                print("tm8: i see a cottage down there lets ask for some place to sleep, and we'll pay them!")
                print("* tm8 knocks at the door of the cottage *")
                time.sleep(3)
                print()
                print("tm8: hey, can we have some place to rest its getting night right here, we can pay ya!\nowner: yeah sure\nyou can also have Some Of My Special fudge if you want?")
                time.sleep(2)
                cottage = input("eat/sleep").replace(" ", "").lower()
                if cottage == "eat":
                    print("you died of poison because the owner was annoyed at night")
                    quit()
                if cottage == "sleep":
                    print("* next morning *")
                    print()
                    time.sleep(1)
                    print("tm8: good morning fella\nlets leave this cottage it stinks like at least have some air spray god damn ")
                    print()
                    time.sleep(2)
                    print("tm8: Im hungry Af but i ain't no eating that cottage,\nalright lets leave and go to McDonald when we find the exit")
                    time.sleep(2)
                    print(" you died of hunger should've tried sth else except of the options ")
                    quit()
                if cottage == "shoot":
                    print("congratulations you beat the game and the owners ass,")
                    print("you now live peacefully with your teammate in the mf's cottage")