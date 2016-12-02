import random
numlist = []
fulllist = list(range(1,101))
guesses = 0
compguess = 50
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
    global compguess
    global guesses
    numlist = list(range(1,101))

    print("The computer will try to guess your number. ")

    user_num = int(input("give me a number between 1 and 100 "))

    guesses += 1
    print("Computer guess is ",compguess)

    counter = (user_num)
    numlist.remove(compguess)

    row = input("Is the computer right? y or n? ")
    while row == "n":
        hilo = input("Is the num higher or lower? h or l? ")
        if hilo == "h":
            compguess = (compguess / 2) + compguess
            compguess = round(compguess,0)


        elif hilo == 'l':
            compguess = compguess - (compguess / 2)
            compguess = round(compguess,0)

        numlist.remove(numlist[0])
        print("Computer guess is ",compguess)
        guesses += 1
        row = input("Is the computer right? y or n? ")


    print("The computer finally guessed your number",compguess)
    print("Since the computer started at 1, it took the computer "\
     ,counter,"tries.")


    return

chrono()
