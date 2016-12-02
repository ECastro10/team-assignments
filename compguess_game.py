'''The user will pick a number between 1 and 100. The computer will start at 1
and keep guessing in increments of 1 until it picks the user number. We will
keep track of the number of guesses it takes for the computer to guess.
We may or may not incorporate a new function.

We'll start by creating a numbers list between 1 and 100
We'll then pick the number 55
Since the computer will begin guessing at numlist[0], everytime the
computer is wrong we'll remove numlist[0]. This loop will break when
computer_guess = user_pick
the count will be user_pick -1.

dirty code for chrono'''
import random
numlist = []
guesses = 0
#usernum = int(input("give us a number "))



def genlist():
    '''
    input: none
    usage:generate a list within a range
    output: is a list with a range called numlist
    '''

    def genlist():
        numlist = list(range(1,101))
        print(numlist)
        return genlist
    genlist()



    pass

def chrono():
    '''
    input:none
    usage: how the computer will chronologically attempt to guess the user
    number in the list. we do this by deleting the numlist[0] and have the
    computer keep guessing numlist[0] in a loop.
    output: will show when the loop breaks when compguess == usernum
    we'll show the count as usernum - 1
    '''
    numlist = list(range(1,101))

    print("The computer will try to guess your number. ")

    user_num = int(input("give me a number between 1 and 100 "))
    compguess = numlist[0]
    print("Computer guess is ",compguess)

    counter = (user_num)
    numlist.remove(numlist[0])
    '''while compguess != user_num:
        numlist.remove(numlist[0])
        compguess = numlist[0]
        print(numlist)'''

    row = input("Is the computer right? y or n? ")
    while row == "n":
        hilo = input("Is the num higher or lower? h or l? ")
        if hilo == "h":
            compguess = numlist[0]
        else:
            compguess = numlist[-1]

        compguess = numlist[0]
        numlist.remove(numlist[0])
        print("Computer guess is ",compguess)
        row = input("Is the computer right? y or n? ")


    print("The computer finally guessed your number",compguess)
    print("Since the computer started at 1, it took the computer "\
     ,counter,"tries.")


    return

def randi():
    '''
    input:none
    usage: we'll have the computer randomly pick a number in a list (rcomp)
    the list's range changes on whether computers choice is greater or lower
    than the usernumber.
    output: The loop breaks when the random number ==usernumber. we'll track
    count of the number of attempts it takes the comp to guess. printing
    the amount of times
    '''
    guesses = 0
    numlist = list(range(1,101))
    rcomp = random.choice(numlist)
    numlist.remove(rcomp)
    guesses += 1
    print('Computer guess is:',rcomp)
    right_or_wrong = input('Is the computer right? (y)es or (n)o? > ')
    while right_or_wrong == 'n':
        rcomp = random.choice(numlist)
        numlist.remove(rcomp)
        print('Computer guess is:',rcomp)
        guesses += 1
        right_or_wrong = input('Is the computer right? (y)es or (n)o? > ')
    print('The computer guessed your number which is',usernum)
    print('It took the computer {} tries'.format(guesses))




def main():
    '''
    input: use global variables: usernum, numlist, guesses
    usage: based on the global numbers we'll see how the computer does using
    two different strategies.
    output: we'll show the number of times it takes the comp to guess using
    the different functions.
    '''

    chrono()
main()
