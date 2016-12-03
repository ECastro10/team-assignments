import math as m
fulllist = list(range(1,101))
guesses = 0

#usernum = int(input("give us a number "))


def chrono():
    '''
    input:none
    usage: how the computer will chronologically attempt to guess the user
    number in the list. we do this by deleting the numlist[0] and have the
    computer keep guessing numlist[0] in a loop.
    output: will show when the loop breaks when compguess == usernum
    we'll show the count as usernum - 1
    '''
    global guesses
    numlist = list(range(1,101))
    compguess = 50
    past_guess = 0
    difference = 0

    print("The computer will try to guess your number. ")

    user_num = int(input("give me a number between 1 and 100 "))
    guesses += 1
    print("Computer guess is ",compguess)

    row = input("Is the computer right? y or n? ")
    while row == "n":
        hilo = input("Is the num higher or lower? h or l? ")
        if hilo == 'h':
            difference = abs(compguess - past_guess)
            print("x-y=",difference)
            difference = (difference / 2)
            difference = m.ceil(difference)
            print("z / 2=",difference)
            past_guess = compguess
            print("y == x",past_guess)
            compguess = compguess + difference
            print("x+z=",compguess)
            if compguess > 100:
                compguess = 100
            guesses += 1


        elif hilo == 'l':
            difference = abs(compguess - past_guess)
            print("x-y=",difference)
            difference = (difference / 2)
            difference = m.ceil(difference)
            print("z / 2=",difference)
            past_guess = compguess
            print("y == x",past_guess)
            compguess = compguess - difference
            print("x+z=",compguess)
            if compguess < 1:
                compguess = 1
            guesses += 1

        print("Computer guess is ",compguess)
        row = input("Is the computer right? y or n? ")


    print("The computer finally guessed your number",guesses)
    print("Since the computer started at 1, it took the computer "\
     ,guesses,"tries.")


    return

chrono()
